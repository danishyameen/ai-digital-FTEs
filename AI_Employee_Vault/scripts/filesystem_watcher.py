"""
filesystem_watcher.py - Monitors the Inbox folder for new files

This watcher detects when files are added to the Inbox folder
and creates corresponding action files in Needs_Action for Claude to process.

Usage:
    python filesystem_watcher.py /path/to/AI_Employee_Vault
"""

import sys
import time
import hashlib
from pathlib import Path
from datetime import datetime

# Import base class
from base_watcher import BaseWatcher

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False
    print("Note: watchdog not installed. Using polling fallback.")


class DropFolderHandler(FileSystemEventHandler):
    """Handles file system events for the Inbox/Drop folder."""
    
    def __init__(self, watcher):
        self.watcher = watcher
        self.logger = watcher.logger
    
    def on_created(self, event):
        """Called when a file or directory is created."""
        if event.is_directory:
            return
        
        source = Path(event.src_path)
        self.logger.info(f'New file detected: {source.name}')
        
        # Small delay to ensure file is fully written
        import time
        time.sleep(0.5)
        
        self.watcher.process_file(source)


class FilesystemWatcher(BaseWatcher):
    """
    Watches the Inbox folder for new files.
    
    When a file is added, it creates a metadata .md file in Needs_Action
    that Claude can process.
    """
    
    def __init__(self, vault_path: str, check_interval: int = 5):
        super().__init__(vault_path, check_interval)
        
        # Track processed files by hash to avoid duplicates
        self.processed_files = {}
        
        # Keywords that indicate priority
        self.priority_keywords = ['urgent', 'asap', 'invoice', 'payment', 'help', 'important']
    
    def check_for_updates(self) -> list:
        """
        Check the Inbox folder for new files.
        
        Returns:
            list: List of new file paths to process
        """
        new_files = []
        
        if not self.inbox.exists():
            return new_files
        
        for file_path in self.inbox.iterdir():
            if file_path.is_file() and not file_path.suffix == '.md':
                # Check if we've already processed this file
                file_hash = self._get_file_hash(file_path)
                if file_path.name not in self.processed_files:
                    self.processed_files[file_path.name] = file_hash
                    new_files.append(file_path)
                elif self.processed_files[file_path.name] != file_hash:
                    # File was modified, reprocess
                    self.logger.info(f'File modified: {file_path.name}')
                    self.processed_files[file_path.name] = file_hash
                    new_files.append(file_path)
        
        return new_files
    
    def _get_file_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of a file."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def process_file(self, file_path: Path):
        """Process a single file and create action file."""
        try:
            self.create_action_file(file_path)
        except Exception as e:
            self.logger.error(f'Error processing file {file_path.name}: {e}')
    
    def create_action_file(self, file_path: Path) -> Path:
        """
        Create a .md action file in Needs_Action folder.
        
        Args:
            file_path: Path to the new file in Inbox
            
        Returns:
            Path: Path to the created action file
        """
        # Read file content if it's text
        content = ""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            self.logger.warning(f'Could not read file content: {e}')
        
        # Check for priority keywords
        content_lower = content.lower()
        priority = 'normal'
        matched_keywords = [kw for kw in self.priority_keywords if kw in content_lower]
        if matched_keywords:
            priority = 'high'
        
        # Get file info
        file_size = file_path.stat().st_size
        timestamp = self.get_timestamp()
        
        # Create action file content
        action_content = f'''---
type: file_drop
original_name: {file_path.name}
size: {file_size}
received: {datetime.now().isoformat()}
priority: {priority}
status: pending
source: filesystem_watcher
---

# File Drop for Processing

## Original File
**Name:** `{file_path.name}`  
**Size:** {self._format_size(file_size)}  
**Location:** `{file_path}`

## Content Preview
```
{content[:1000] if content else '(Binary file or unreadable)'}
```

## Suggested Actions
- [ ] Review file content
- [ ] Categorize file
- [ ] Take appropriate action
- [ ] Move to /Done when complete

## Processing Notes
<!-- Add notes here as Claude processes this file -->

'''
        
        # Create filename for action file
        safe_name = self.sanitize_filename(file_path.name)
        action_filename = f'FILE_{safe_name}_{timestamp}.md'
        action_path = self.needs_action / action_filename
        
        # Write action file
        action_path.write_text(action_content)
        
        self.logger.info(f'Created action file: {action_filename}')
        
        return action_path
    
    def _format_size(self, size: int) -> str:
        """Format file size in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"
    
    def run_with_watchdog(self):
        """Run using watchdog for real-time file monitoring."""
        if not WATCHDOG_AVAILABLE:
            self.logger.warning('watchdog not available, using polling mode')
            self.run()
            return
        
        self.logger.info(f'Starting {self.__class__.__name__} (watchdog mode)')
        self.logger.info(f'Watching: {self.inbox}')
        
        event_handler = DropFolderHandler(self)
        observer = Observer()
        observer.schedule(event_handler, str(self.inbox), recursive=False)
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            self.logger.info('FilesystemWatcher stopped')
        observer.join()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python filesystem_watcher.py <vault_path>")
        print("Example: python filesystem_watcher.py ./AI_Employee_Vault")
        sys.exit(1)
    
    vault_path = sys.argv[1]
    
    if not Path(vault_path).exists():
        print(f"Error: Vault path does not exist: {vault_path}")
        sys.exit(1)
    
    watcher = FilesystemWatcher(vault_path)
    
    # Use watchdog if available, otherwise fall back to polling
    if WATCHDOG_AVAILABLE:
        watcher.run_with_watchdog()
    else:
        watcher.run()


if __name__ == '__main__':
    main()
