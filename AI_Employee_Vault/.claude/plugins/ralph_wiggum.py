"""
Ralph Wiggum Stop Hook Plugin for Qwen Code

This plugin intercepts Qwen's attempt to exit and checks if tasks are complete.
If tasks are incomplete, it blocks the exit and re-injects the prompt.

Installation:
1. Copy this file to: AI_Employee_Vault/.claude/plugins/ralph_wiggum.py
2. Enable in Qwen Code settings

Usage:
    /ralph-loop "Process all files in /Needs_Action" --max-iterations 10
"""

import os
import sys
from pathlib import Path
from datetime import datetime


class RalphWiggumPlugin:
    """
    Ralph Wiggum Stop Hook Plugin.

    Keeps Qwen Code iterating until tasks are complete.
    Named after the Simpsons character who never gives up.
    """
    
    def __init__(self, vault_path: str, max_iterations: int = 10):
        """
        Initialize the plugin.
        
        Args:
            vault_path: Path to the Obsidian vault
            max_iterations: Maximum number of iterations before forcing stop
        """
        self.vault_path = Path(vault_path)
        self.max_iterations = max_iterations
        self.current_iteration = 0
        
        # Key folders
        self.needs_action = self.vault_path / 'Needs_Action'
        self.done = self.vault_path / 'Done'
        self.pending_approval = self.vault_path / 'Pending_Approval'
        self.plans = self.vault_path / 'Plans'
        
        # State file to track iterations
        self.state_file = self.vault_path / '.ralph_state.md'
    
    def load_state(self) -> dict:
        """Load current state from file."""
        if not self.state_file.exists():
            return {'iteration': 0, 'last_check': None}
        
        try:
            content = self.state_file.read_text()
            iteration = 0
            for line in content.split('\n'):
                if line.startswith('iteration:'):
                    iteration = int(line.split(':')[1].strip())
            return {'iteration': iteration, 'last_check': datetime.now()}
        except Exception:
            return {'iteration': 0, 'last_check': None}
    
    def save_state(self, state: dict):
        """Save current state to file."""
        content = f"""---
iteration: {state.get('iteration', 0)}
last_check: {datetime.now().isoformat()}
max_iterations: {self.max_iterations}
---

# Ralph Wiggum State

This file tracks the current iteration of the Ralph Wiggum loop.
"""
        self.state_file.write_text(content)
    
    def check_completion(self) -> tuple[bool, str]:
        """
        Check if all tasks are complete.
        
        Returns:
            tuple: (is_complete, reason)
        """
        # Check Needs_Action folder
        pending_count = len(list(self.needs_action.glob('*.md')))
        if pending_count > 0:
            return False, f'{pending_count} items still in Needs_Action'
        
        # Check Plans folder for incomplete plans
        plans_folder = self.plans
        if plans_folder.exists():
            for plan_file in plans_folder.glob('*.md'):
                content = plan_file.read_text()
                # Check for unchecked items
                if '- [ ]' in content:
                    return False, f'Incomplete plan: {plan_file.name}'
        
        # Check Pending_Approval (these are waiting on human, not Claude)
        # This is OK - Claude can exit if only pending_approval items remain
        
        return True, 'All tasks complete'
    
    def should_stop(self) -> tuple[bool, str]:
        """
        Determine if Claude should be allowed to stop.
        
        Returns:
            tuple: (should_stop, reason)
        """
        self.current_iteration += 1
        state = self.load_state()
        state['iteration'] = self.current_iteration
        self.save_state(state)
        
        # Check max iterations
        if self.current_iteration >= self.max_iterations:
            return True, f'Max iterations ({self.max_iterations}) reached'
        
        # Check task completion
        is_complete, reason = self.check_completion()
        if is_complete:
            return True, reason
        
        # Tasks not complete - don't stop
        return False, f'Tasks incomplete: {reason}'
    
    def on_exit_attempt(self, context: dict) -> dict:
        """
        Called when Claude attempts to exit.
        
        Args:
            context: Current execution context
            
        Returns:
            dict: Modified context (with new prompt if continuing)
        """
        should_stop, reason = self.should_stop()
        
        if should_stop:
            # Allow exit
            context['allow_exit'] = True
            context['exit_message'] = f'Ralph Wiggum: {reason}'
        else:
            # Block exit and continue
            context['allow_exit'] = False
            context['continue_prompt'] = f'''
<RALPH_WIGGUM_LOOP>
Task incomplete: {reason}
Iteration: {self.current_iteration}/{self.max_iterations}

Continue working on the pending items. 
Check /Needs_Action folder and process any remaining files.
If waiting for human approval, note that in the status.
</RALPH_WIGGUM_LOOP>
'''
        
        return context


def ralph_loop(vault_path: str, prompt: str, max_iterations: int = 10):
    """
    Start a Ralph Wiggum loop.
    
    Args:
        vault_path: Path to the vault
        prompt: Initial prompt for Claude
        max_iterations: Maximum iterations
    """
    plugin = RalphWiggumPlugin(vault_path, max_iterations)
    
    print(f"Starting Ralph Wiggum loop")
    print(f"Vault: {vault_path}")
    print(f"Max iterations: {max_iterations}")
    print(f"Prompt: {prompt[:100]}...")
    print("-" * 50)
    
    # This would integrate with Claude Code's plugin system
    # For now, it's a reference implementation
    return plugin


# CLI entry point
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Ralph Wiggum Stop Hook')
    parser.add_argument('vault_path', help='Path to Obsidian vault')
    parser.add_argument('--prompt', '-p', help='Initial prompt', default='')
    parser.add_argument('--max-iterations', '-m', type=int, default=10,
                       help='Maximum iterations')
    
    args = parser.parse_args()
    
    plugin = RalphWiggumPlugin(args.vault_path, args.max_iterations)
    
    # Run completion check
    is_complete, reason = plugin.check_completion()
    print(f"Task complete: {is_complete}")
    print(f"Reason: {reason}")
