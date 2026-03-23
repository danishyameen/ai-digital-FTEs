# AI Employee Vault - Bronze Tier

Your Personal AI Employee workspace. This vault serves as the memory, dashboard, and control center for your autonomous AI agent.

## Quick Start

### 1. Open in Obsidian

```bash
# Open this vault in Obsidian
obsidian://open?vault=AI_Employee_Vault
```

Or manually:
1. Open Obsidian
2. Click "Open folder as vault"
3. Select this `AI_Employee_Vault` folder

### 2. Start the Filesystem Watcher

```bash
# Navigate to the vault
cd AI_Employee_Vault/scripts

# Install watchdog (optional, for real-time monitoring)
pip install watchdog

# Start the watcher
python filesystem_watcher.py ..
```

### 3. Start the Orchestrator

In a new terminal:

```bash
cd AI_Employee_Vault/scripts
python orchestrator.py ..
```

### 4. Test the System

1. Create a test file in the `Inbox` folder:
   ```bash
   echo "This is a test task. Please process this request." > Inbox/test_task.txt
   ```

2. Watch the watcher create an action file in `Needs_Action/`

3. The orchestrator will trigger Claude Code to process it

4. Claude will read `Company_Handbook.md` for rules and create a plan

## Folder Structure

```
AI_Employee_Vault/
├── Dashboard.md              # Main status dashboard
├── Company_Handbook.md       # Rules and procedures
├── Business_Goals.md         # Your objectives and targets
├── Inbox/                    # Drop files here for processing
├── Needs_Action/             # Items awaiting AI processing
├── Pending_Approval/         # Actions waiting for human approval
├── Approved/                 # Approved actions ready to execute
├── Plans/                    # Multi-step task plans
├── Done/                     # Completed items
└── Logs/                     # System logs
```

## Key Files

| File | Purpose |
|------|---------|
| `Dashboard.md` | Real-time status overview |
| `Company_Handbook.md` | AI employee rules and guidelines |
| `Business_Goals.md` | Your business objectives and metrics |

## How It Works

1. **Watcher** monitors `Inbox/` for new files
2. When a file is detected, creates action file in `Needs_Action/`
3. **Orchestrator** creates a prompt file for Qwen Code
4. **User runs Qwen Code** manually to process pending items
5. Qwen reads `Company_Handbook.md` for rules
6. Qwen creates `Plan.md` for multi-step tasks
7. Sensitive actions go to `Pending_Approval/`
8. Human moves files to `Approved/` to authorize
9. Qwen executes approved actions
10. Completed items move to `Done/`

## Qwen Code Commands

```bash
# Navigate to vault directory
cd AI_Employee_Vault

# Start Qwen Code interactively
qwen

# Then paste the prompt from .qwen_pending.md
# Or manually prompt:
# "Process all files in /Needs_Action folder"
```

### Processing Workflow

When the orchestrator detects pending items, it creates `.qwen_pending.md` with the prompt.

**To process:**
1. Open terminal in vault directory
2. Run `qwen`
3. Copy prompt from `.qwen_pending.md`
4. Qwen will process and create plans

## Requirements

- **Python 3.13+** - For watcher scripts
- **Qwen Code** - Active subscription
- **Obsidian** - v1.10.6+ (free)
- **watchdog** (optional) - For real-time file monitoring

## Troubleshooting

### Watcher not detecting files
- Ensure the `Inbox` folder exists
- Check logs in `Logs/` folder
- Try running with `--verbose` flag

### Qwen Code not found
```bash
# Install Qwen Code
# Follow the installation instructions for your platform

# Verify installation
qwen --version
```

### Permission errors
- Make sure you have read/write access to the vault folder
- On Windows, run terminal as Administrator if needed

## Next Steps (Silver Tier)

After mastering Bronze tier, enhance your AI Employee with:

- [ ] Gmail Watcher integration
- [ ] WhatsApp Watcher integration
- [ ] MCP server for email sending
- [ ] Approval workflow automation
- [ ] Scheduled tasks (cron/Task Scheduler)

## Support

For issues or questions:
- Check logs in `Logs/` folder
- Review `Company_Handbook.md` for rules
- Join weekly Wednesday meetings: https://us06web.zoom.us/j/87188707642?pwd=a9XloCsinvn1JzICbPc2YGUvWTbOTr.1

---

*AI Employee v0.1 (Bronze Tier) - Built with Qwen Code & Obsidian*
