"""
base_watcher.py - Base class for all Watcher scripts

Watchers are lightweight Python scripts that run continuously,
monitoring various inputs and creating actionable files for Claude to process.
"""

import time
import logging
from pathlib import Path
from abc import ABC, abstractmethod
from datetime import datetime


class BaseWatcher(ABC):
    """
    Abstract base class for all watcher scripts.
    
    All watchers follow this pattern:
    1. Monitor a specific input source (Gmail, WhatsApp, filesystem, etc.)
    2. Detect new/unprocessed items
    3. Create .md files in the Needs_Action folder
    4. Claude Code processes these files and takes action
    """
    
    def __init__(self, vault_path: str, check_interval: int = 60):
        """
        Initialize the watcher.
        
        Args:
            vault_path: Path to the Obsidian vault root
            check_interval: How often to check for updates (in seconds)
        """
        self.vault_path = Path(vault_path)
        self.needs_action = self.vault_path / 'Needs_Action'
        self.inbox = self.vault_path / 'Inbox'
        self.logs = self.vault_path / 'Logs'
        self.check_interval = check_interval
        
        # Ensure directories exist
        self.needs_action.mkdir(parents=True, exist_ok=True)
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.logs.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        self._setup_logging()
        
        # Track processed items to avoid duplicates
        self.processed_ids = set()
        
    def _setup_logging(self):
        """Setup logging to file and console."""
        log_file = self.logs / f'watcher_{datetime.now().strftime("%Y-%m-%d")}.log'
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def check_for_updates(self) -> list:
        """
        Check for new items to process.
        
        Returns:
            list: List of new items (format depends on watcher type)
        """
        pass
    
    @abstractmethod
    def create_action_file(self, item) -> Path:
        """
        Create a .md file in Needs_Action folder for the item.
        
        Args:
            item: The item to process (format depends on watcher type)
            
        Returns:
            Path: Path to the created action file
        """
        pass
    
    def run(self):
        """
        Main run loop for the watcher.
        
        Continuously checks for updates and creates action files.
        Runs until interrupted (Ctrl+C).
        """
        self.logger.info(f'Starting {self.__class__.__name__}')
        self.logger.info(f'Vault path: {self.vault_path}')
        self.logger.info(f'Check interval: {self.check_interval}s')
        
        try:
            while True:
                try:
                    items = self.check_for_updates()
                    for item in items:
                        try:
                            action_file = self.create_action_file(item)
                            self.logger.info(f'Created action file: {action_file.name}')
                        except Exception as e:
                            self.logger.error(f'Error creating action file: {e}')
                except Exception as e:
                    self.logger.error(f'Error checking for updates: {e}')
                
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.logger.info(f'{self.__class__.__name__} stopped by user')
        except Exception as e:
            self.logger.error(f'Fatal error: {e}')
            raise
    
    def sanitize_filename(self, name: str) -> str:
        """
        Sanitize a string to be used as a filename.
        
        Args:
            name: The original name
            
        Returns:
            str: Sanitized filename safe for all platforms
        """
        # Remove or replace invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            name = name.replace(char, '_')
        return name
    
    def get_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
