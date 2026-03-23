"""
test_watcher.py - Quick test script for the Filesystem Watcher
"""

from pathlib import Path
import sys

# Add scripts directory to path
scripts_dir = Path(__file__).parent / 'scripts'
sys.path.insert(0, str(scripts_dir))

from filesystem_watcher import FilesystemWatcher

def main():
    vault_path = Path(__file__).parent
    print(f"Vault path: {vault_path}")
    print(f"Inbox exists: {(vault_path / 'Inbox').exists()}")
    print(f"Needs_Action exists: {(vault_path / 'Needs_Action').exists()}")
    
    # Create watcher
    watcher = FilesystemWatcher(str(vault_path))
    print(f"Watcher created")
    
    # Check for files
    files = watcher.check_for_updates()
    print(f"Files found: {len(files)}")
    
    for f in files:
        print(f"  Processing: {f.name}")
        action_file = watcher.create_action_file(f)
        print(f"  Created action file: {action_file.name}")
    
    print("\nDone!")

if __name__ == '__main__':
    main()
