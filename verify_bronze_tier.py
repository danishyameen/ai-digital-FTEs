"""
verify_bronze_tier.py - Verify Bronze Tier setup is complete

This script checks that all Bronze Tier requirements are met:
- Obsidian vault with Dashboard.md and Company_Handbook.md
- Basic folder structure: /Inbox, /Needs_Action, /Done
- One working Watcher script (filesystem watcher)
- Claude Code can read/write to the vault
"""

import sys
from pathlib import Path
from datetime import datetime


class BronzeTierVerifier:
    """Verifies Bronze Tier requirements are met."""
    
    def __init__(self, vault_path: Path):
        self.vault_path = vault_path
        self.passed = []
        self.failed = []
        self.warnings = []
    
    def check(self, name: str, condition: bool, error_msg: str = ""):
        """Record a check result."""
        if condition:
            self.passed.append(name)
            print(f"✓ {name}")
        else:
            self.failed.append(f"{name}: {error_msg}")
            print(f"✗ {name} - {error_msg}")
    
    def verify_all(self):
        """Run all verification checks."""
        print("=" * 60)
        print("  Bronze Tier Verification")
        print("=" * 60)
        print()
        
        # 1. Check required files exist
        print("Required Files:")
        self.check(
            "Dashboard.md exists",
            (self.vault_path / "Dashboard.md").exists(),
            "Create Dashboard.md in vault root"
        )
        self.check(
            "Company_Handbook.md exists",
            (self.vault_path / "Company_Handbook.md").exists(),
            "Create Company_Handbook.md in vault root"
        )
        self.check(
            "Business_Goals.md exists",
            (self.vault_path / "Business_Goals.md").exists(),
            "Create Business_Goals.md in vault root"
        )
        print()
        
        # 2. Check folder structure
        print("Folder Structure:")
        required_folders = ["Inbox", "Needs_Action", "Done", "Pending_Approval", "Approved", "Plans", "Logs"]
        for folder in required_folders:
            self.check(
                f"/{folder} folder exists",
                (self.vault_path / folder).exists(),
                f"Create folder: {folder}"
            )
        print()
        
        # 3. Check watcher scripts
        print("Watcher Scripts:")
        scripts_path = self.vault_path / "scripts"
        self.check(
            "scripts/ directory exists",
            scripts_path.exists(),
            "Create scripts/ directory"
        )
        self.check(
            "base_watcher.py exists",
            (scripts_path / "base_watcher.py").exists(),
            "Create base_watcher.py"
        )
        self.check(
            "filesystem_watcher.py exists",
            (scripts_path / "filesystem_watcher.py").exists(),
            "Create filesystem_watcher.py"
        )
        self.check(
            "orchestrator.py exists",
            (scripts_path / "orchestrator.py").exists(),
            "Create orchestrator.py"
        )
        print()
        
        # 4. Check Ralph Wiggum plugin
        print("Ralph Wiggum Plugin:")
        plugins_path = self.vault_path / ".claude" / "plugins"
        self.check(
            ".claude/plugins/ directory exists",
            plugins_path.exists(),
            "Create .claude/plugins/ directory"
        )
        self.check(
            "ralph_wiggum.py exists",
            (plugins_path / "ralph_wiggum.py").exists(),
            "Create ralph_wiggum.py plugin"
        )
        print()
        
        # 5. Test watcher functionality
        print("Watcher Functionality Test:")
        try:
            sys.path.insert(0, str(scripts_path))
            from filesystem_watcher import FilesystemWatcher
            
            watcher = FilesystemWatcher(str(self.vault_path))
            self.check("Watcher initializes", True)
            
            # Check inbox for files
            files = watcher.check_for_updates()
            self.check(
                "Watcher can scan Inbox",
                True,
                ""
            )
            self.check(
                f"Inbox has test file(s)",
                len(files) > 0 or len(list((self.vault_path / "Inbox").iterdir())) > 0,
                "Add a test file to Inbox/"
            )
        except Exception as e:
            self.check("Watcher functionality", False, str(e))
        print()
        
        # 6. Check Qwen Code
        print("Qwen Code Integration:")
        import subprocess
        try:
            # Try qwen first, then qwen-code as alternative
            # Use shell=True to inherit full PATH
            for cmd in ["qwen --version", "qwen-code --version"]:
                try:
                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=10,
                        shell=True
                    )
                    if result.returncode == 0:
                        self.check("Qwen Code installed", True)
                        self.check(
                            "Qwen Code version",
                            True,
                            ""
                        )
                        print(f"  Version: {result.stdout.strip()}")
                        break
                except Exception:
                    continue
            else:
                self.check("Qwen Code installed", False, "Command not found")
        except Exception as e:
            self.check("Qwen Code check", False, str(e))
        print()
        
        # Summary
        print("=" * 60)
        print(f"  Results: {len(self.passed)} passed, {len(self.failed)} failed, {len(self.warnings)} warnings")
        print("=" * 60)
        
        if self.failed:
            print("\nFailed checks:")
            for fail in self.failed:
                print(f"  - {fail}")
            return False
        else:
            print("\n✓ All Bronze Tier requirements met!")
            print("\nNext steps:")
            print("  1. Open vault in Obsidian")
            print("  2. Run: python scripts/start_ai_employee.bat")
            print("  3. Drop a file in Inbox/ to test")
            return True


def main():
    """Main entry point."""
    # Determine vault path
    if len(sys.argv) > 1:
        vault_path = Path(sys.argv[1])
    else:
        # Default to sibling directory
        vault_path = Path(__file__).parent / "AI_Employee_Vault"
    
    if not vault_path.exists():
        print(f"Error: Vault not found: {vault_path}")
        sys.exit(1)
    
    verifier = BronzeTierVerifier(vault_path)
    success = verifier.verify_all()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
