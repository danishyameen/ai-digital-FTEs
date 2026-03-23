# AI Digital FTEs - Personal AI Employee (Bronze Tier)

> **Tagline:** Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.

This repository contains a **working implementation** of a Personal AI Employee (Digital FTE) - an autonomous AI agent that manages personal and business affairs 24/7 using **Qwen Code** and **Obsidian**.

**Current Status:** ✅ **Bronze Tier Complete** (21/21 checks passed)

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **Tier** | Bronze (Foundation) |
| **Primary AI** | Qwen Code v0.12.6 |
| **Knowledge Base** | Obsidian Markdown |
| **Architecture** | Local-first, Privacy-focused |
| **Verification** | ✅ 21/21 checks passed |
| **Time to Build** | 8-12 hours |

---

## 🎯 What is Bronze Tier?

Bronze Tier is the **minimum viable deliverable** for the AI Employee hackathon. It provides the foundational layer for autonomous AI automation.

### Bronze Tier Deliverables (All Complete ✅)

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | Obsidian vault with Dashboard.md | ✅ Complete |
| 2 | Company_Handbook.md with rules | ✅ Complete |
| 3 | Business_Goals.md template | ✅ Complete |
| 4 | Basic folder structure | ✅ Complete |
| 5 | One working Watcher (Filesystem) | ✅ Complete |
| 6 | Qwen Code integration | ✅ Complete |
| 7 | Ralph Wiggum plugin | ✅ Complete |

---

## 📁 Repository Structure

```
ai-digital-FTEs/
│
├── 📄 README.md                          # This file - Bronze Tier summary
├── 📄 Personal AI Employee Hackathon...  # Main blueprint (1201 lines)
├── 📄 QWEN.md                            # AI assistant context
├── 📄 skills-lock.json                   # Installed skills tracker
├── 📄 verify_bronze_tier.py              # Verification script (21 checks)
│
├── 📂 .qwen/                             # Qwen Code configurations
│   └── skills/
│       └── browsing-with-playwright/     # Web automation skill (for future tiers)
│
└── 📂 AI_Employee_Vault/                 # 🏠 Obsidian Vault (AI Employee Workspace)
    ├── 📄 Dashboard.md                   # Real-time status dashboard
    ├── 📄 Company_Handbook.md            # Rules and procedures
    ├── 📄 Business_Goals.md              # Objectives and metrics
    ├── 📄 README.md                      # Vault-specific instructions
    │
    ├── 📂 Inbox/                         # Drop files here for processing
    ├── 📂 Needs_Action/                  # Items awaiting AI processing
    ├── 📂 Pending_Approval/              # Awaiting human approval
    ├── 📂 Approved/                      # Ready for execution
    ├── 📂 Plans/                         # Multi-step task plans
    ├── 📂 Done/                          # Completed items
    ├── 📂 Logs/                          # System logs
    ├── 📂 Accounting/                    # Financial records
    ├── 📂 Invoices/                      # Generated invoices
    └── 📂 scripts/                       # Automation scripts
        ├── base_watcher.py               # Base class for all watchers
        ├── filesystem_watcher.py         # Monitors Inbox folder (Bronze)
        ├── orchestrator.py               # Triggers Qwen Code
        ├── requirements.txt              # Python dependencies
        ├── start_ai_employee.bat         # Windows startup script
        └── ralph_wiggum.py               # Stop hook for continuous iteration
```

---

## 🏗️ Bronze Tier Architecture

### Simple Flow: Perception → Reasoning → Action

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   PERCEPTION    │────▶│    REASONING    │────▶│     ACTION      │
│                 │     │                 │     │                 │
│ File Watcher    │     │ Qwen Code       │     │ Manual Execute  │
│ (filesystem)    │     │ (interactive)   │     │ (via Qwen)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
  Creates .md files      Creates .qwen_         User runs qwen
  in Needs_Action/       pending.md             and pastes prompt
```

### Key Components (Bronze Tier)

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Brain** | Qwen Code | Reasoning engine, decision making |
| **Memory** | Obsidian | Dashboard, handbook, knowledge base |
| **Senses** | Filesystem Watcher | Monitors Inbox folder for new files |
| **Hands** | User + Qwen | Manual execution via Qwen Code |

**Note:** Bronze Tier uses **manual Qwen execution**. Silver Tier adds automated MCP servers.

---

## 🚀 Quick Start

### Prerequisites

| Component | Version | Install Command |
|-----------|---------|-----------------|
| Python | 3.13+ | [python.org](https://python.org) |
| Qwen Code | Latest | `pip install qwen-code` |
| Obsidian | v1.10.6+ | [obsidian.md](https://obsidian.md) |
| watchdog | 3.0.0+ | `pip install watchdog` |

### Installation (5 minutes)

```bash
# 1. Navigate to the repository
cd C:\Users\Evantagers\Documents\GitHub\ai-digital-FTEs

# 2. Install Python dependencies
cd AI_Employee_Vault\scripts
pip install -r requirements.txt

# 3. Verify Bronze Tier setup
cd ../..
python verify_bronze_tier.py AI_Employee_Vault
```

**Expected output:** `✓ All Bronze Tier requirements met!`

### Running the AI Employee

**Step 1: Start the watchers**
```cmd
cd AI_Employee_Vault
scripts\start_ai_employee.bat
```

This opens two terminal windows:
- **Filesystem Watcher** - Monitors `Inbox/` for new files
- **Orchestrator** - Creates prompts for Qwen Code

**Step 2: Test the system**
```bash
# Drop a test file in Inbox
echo "Process this request" > Inbox/test.txt
```

**Step 3: Process with Qwen Code**
```bash
cd AI_Employee_Vault
qwen
# Copy prompt from .qwen_pending.md and paste
```

---

## 🔄 How It Works (Bronze Tier)

### Complete Workflow

```
1. User drops file in Inbox/
        ↓
2. Filesystem Watcher detects new file (within 5 seconds)
        ↓
3. Creates action file in Needs_Action/
        ↓
4. Orchestrator detects pending item (every 30 seconds)
        ↓
5. Creates .qwen_pending.md with prompt
        ↓
6. User runs: qwen
        ↓
7. Qwen reads Company_Handbook.md for rules
        ↓
8. Qwen creates Plan.md for multi-step tasks
        ↓
9. Qwen moves completed items to Done/
```

### Example: Processing a Test File

```
📥 Inbox/test_task.txt
    ↓ (Filesystem Watcher detects)
📋 Needs_Action/FILE_test_task_2026-03-23_03-33-08.md
    ↓ (Orchestrator creates prompt)
📝 .qwen_pending.md
    ↓ (User runs Qwen)
🤖 Qwen reads and processes
    ↓ (Creates plan if needed)
📝 Plans/test_task_Plan.md
    ↓ (Completes task)
✅ Done/FILE_test_task_...md
```

---

## 📂 File Descriptions

### Root Level Files

| File | Purpose |
|------|---------|
| `README.md` | This Bronze Tier summary |
| `Personal AI Employee Hackathon 0_...md` | Complete architectural blueprint (1201 lines) |
| `QWEN.md` | Context file for AI assistants |
| `skills-lock.json` | Tracks installed Qwen skills |
| `verify_bronze_tier.py` | Verification script (21 checks) |

### AI_Employee_Vault Core Files

| File | Purpose |
|------|---------|
| `Dashboard.md` | Real-time status, metrics, alerts |
| `Company_Handbook.md` | AI employee rules (response times, approval thresholds) |
| `Business_Goals.md` | Revenue targets, key metrics, subscription list |
| `README.md` | Vault-specific usage instructions |

### Scripts (Bronze Tier)

| File | Purpose |
|------|---------|
| `base_watcher.py` | Abstract base class for all watchers |
| `filesystem_watcher.py` | **Bronze:** Monitors Inbox for new files |
| `orchestrator.py` | Triggers Qwen Code on pending items |
| `start_ai_employee.bat` | Windows startup script |
| `ralph_wiggum.py` | Stop hook for continuous iteration |

---

## 📊 Current Vault Status

### Folder Contents

| Folder | Purpose | Current Items |
|--------|---------|---------------|
| `Inbox/` | Drop files here | 7 files |
| `Needs_Action/` | Awaiting processing | 0 files |
| `Plans/` | Multi-step task plans | 6 files |
| `Pending_Approval/` | Awaiting human approval | 0 files |
| `Approved/` | Ready for execution | 10 files |
| `Done/` | Completed tasks | 10 files |
| `Invoices/` | Generated invoices | 3 files |
| `Logs/` | System logs | 5 files |

### Generated Documents

**Invoices:**
- INV-2026-001.md
- INV-2026-002.md
- INV-2026-003.md

**Plans:**
- Invoice_5000_Plan.md
- Payment_Receipt_DanishYameen_10000_Plan.md
- Utility_Bill_8000_Plan.md
- (and 3 more)

**Approvals:**
- Sales_Invoice_DanishYameen_10000_Approval.md
- Utility_Bill_8000_Approval.md
- (and 8 more)

---

## 🔧 Configuration

### Python Dependencies

```txt
# requirements.txt
watchdog>=3.0.0
```

### Verify Qwen Code

```bash
qwen --version
# Expected: 0.12.6
```

### Verify Bronze Tier

```bash
python verify_bronze_tier.py AI_Employee_Vault
```

**Expected output:**
```
============================================================
  Bronze Tier Verification
============================================================
✓ Dashboard.md exists
✓ Company_Handbook.md exists
✓ Business_Goals.md exists
✓ /Inbox folder exists
✓ /Needs_Action folder exists
...
============================================================
  Results: 21 passed, 0 failed, 0 warnings
============================================================
✓ All Bronze Tier requirements met!
```

---

## 📝 Meeting Information

**Weekly Research & Showcase**
- **When:** Wednesdays at 10:00 PM PKT
- **Zoom:** [Join Meeting](https://us06web.zoom.us/j/87188707642?pwd=a9XloCsinvn1JzICbPc2YGUvWTbOTr.1)
- **Meeting ID:** 871 8870 7642
- **Passcode:** 744832
- **YouTube:** [@panaversity](https://www.youtube.com/@panaversity)

---

## 🎓 Learning Resources

### Prerequisites (Already Complete ✅)

| Topic | Status |
|-------|--------|
| Qwen Code Fundamentals | ✅ Complete |
| Obsidian Fundamentals | ✅ Complete |
| Python File I/O | ✅ Complete |
| Agent Skills | ✅ Complete |

### For Next Tier (Silver)

| Topic | Resource |
|-------|----------|
| Gmail API | developers.google.com/gmail/api |
| MCP Servers | modelcontextprotocol.io |
| Playwright | playwright.dev/python |

---

## 🚨 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Watcher not detecting files | Check `Inbox/` exists, view `Logs/watcher_*.log` |
| Qwen not found | Run `qwen --version`, ensure it's in PATH |
| Permission errors | Run terminal as Administrator |
| Orchestrator not creating prompts | Check `Logs/orchestrator_*.log` |

### Log Files

Check these files for debugging:
- `Logs/watcher_2026-03-23.log` - Filesystem Watcher logs
- `Logs/orchestrator_2026-03-23.log` - Orchestrator logs

### Getting Help

1. Check logs in `AI_Employee_Vault/Logs/`
2. Review `Company_Handbook.md` for rules
3. Run verification: `python verify_bronze_tier.py AI_Employee_Vault`
4. Join Wednesday meetings for support

---

## 📈 What's Next? (After Bronze)

### Silver Tier Upgrades

| Feature | Bronze | Silver |
|---------|--------|--------|
| Watchers | Filesystem only | Gmail + WhatsApp + LinkedIn |
| Action Execution | Manual (via Qwen) | Automated (via MCP) |
| Approval Workflow | Manual file move | Automated detection |
| Scheduling | Manual | cron/Task Scheduler |

### To Upgrade to Silver

1. Add Gmail Watcher (uses Google API)
2. Add WhatsApp Watcher (uses Playwright)
3. Create MCP server for email sending
4. Automate approval detection
5. Add scheduled tasks

---

## 📄 Credits

**Project:** AI Digital FTEs - Personal AI Employee  
**Tier:** Bronze (Foundation)  
**Implementation Status:** ✅ Complete  
**AI Engine:** Qwen Code v0.12.6  
**Knowledge Base:** Obsidian Markdown  
**Blueprint:** 1201-line hackathon guide  

---

*AI Employee v0.1 (Bronze Tier) - Built with Qwen Code & Obsidian*  
*Last Updated: March 23, 2026*  
*Verification: 21/21 checks passed*
