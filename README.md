# AI Digital FTEs - Personal AI Employee Hackathon

> **Tagline:** Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.

This repository contains the complete blueprint and working implementation for building **Personal AI Employees** (Digital FTEs) - autonomous AI agents that manage personal and business affairs 24/7 using **Qwen Code** and **Obsidian**.

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **Project Type** | AI Automation Framework |
| **Primary AI** | Qwen Code |
| **Knowledge Base** | Obsidian Markdown |
| **Architecture** | Local-first, Privacy-focused |
| **Status** | ✅ Bronze Tier Complete |
| **Verification** | 21/21 checks passed |

---

## 🎯 Core Concept

Build an AI agent that works like a human employee but with:

| Feature | Human FTE | Digital FTE |
|---------|-----------|-------------|
| Availability | 40 hours/week | **168 hours/week** (24/7) |
| Monthly Cost | $4,000 – $8,000+ | **$500 – $2,000** |
| Ramp-up Time | 3 – 6 Months | **Instant** |
| Consistency | 85–95% accuracy | **99%+ consistency** |
| Cost per Task | ~$5.00 | **~$0.50** |

**💡 The 'Aha!' Moment:** 85-90% cost reduction compared to human employees.

---

## 📁 Repository Structure

```
ai-digital-FTEs/
│
├── 📄 README.md                          # This file - Complete project summary
├── 📄 Personal AI Employee Hackathon...  # Main blueprint (1201 lines)
├── 📄 QWEN.md                            # AI assistant context
├── 📄 skills-lock.json                   # Installed skills tracker
├── 📄 verify_bronze_tier.py              # Verification script
│
├── 📂 .qwen/                             # Qwen Code configurations
│   └── skills/
│       └── browsing-with-playwright/     # Web automation skill
│           ├── SKILL.md
│           ├── references/
│           │   └── playwright-tools.md
│           └── scripts/
│               ├── mcp-client.py
│               ├── start-server.sh
│               ├── stop-server.sh
│               └── verify.py
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
        ├── base_watcher.py               # Base class for watchers
        ├── filesystem_watcher.py         # Monitors Inbox folder
        ├── orchestrator.py               # Triggers Qwen Code
        ├── requirements.txt              # Python dependencies
        └── start_ai_employee.bat         # Windows startup script
```

---

## 🏗️ Architecture

### Perception → Reasoning → Action

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   PERCEPTION    │────▶│    REASONING    │────▶│     ACTION      │
│                 │     │                 │     │                 │
│ • File Watchers │     │ • Qwen Code     │     │ • MCP Servers   │
│ • Gmail API     │     │ • Plan.md       │     │ • Email Send    │
│ • WhatsApp      │     │ • Decision Tree │     │ • Browser Auto  │
│ • Bank APIs     │     │ • Handbook Rules│     │ • Payments      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
  Creates .md files      Creates plans          Executes tasks
  in Needs_Action/       in Plans/              Moves to Done/
```

### Key Components

| Layer | Component | Technology | Purpose |
|-------|-----------|------------|---------|
| **Brain** | Qwen Code | AI LLM | Reasoning engine, decision making |
| **Memory** | Obsidian | Markdown | Dashboard, handbook, knowledge base |
| **Senses** | Watchers | Python | Monitor Gmail, WhatsApp, filesystems |
| **Hands** | MCP Servers | Node.js/Python | Execute external actions |

---

## 🚀 Quick Start

### Prerequisites

| Component | Version | Install |
|-----------|---------|---------|
| Python | 3.13+ | [python.org](https://python.org) |
| Qwen Code | Latest | `pip install qwen-code` |
| Obsidian | v1.10.6+ | [obsidian.md](https://obsidian.md) |
| Node.js | v24+ LTS | [nodejs.org](https://nodejs.org) |

### Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd ai-digital-FTEs

# 2. Install Python dependencies
cd AI_Employee_Vault/scripts
pip install -r requirements.txt

# 3. Verify setup
cd ../..
python verify_bronze_tier.py AI_Employee_Vault
```

### Running the AI Employee

**Option 1: Using the batch file (Windows)**
```cmd
cd AI_Employee_Vault
scripts\start_ai_employee.bat
```

**Option 2: Manual start**
```bash
# Terminal 1: Start Filesystem Watcher
cd AI_Employee_Vault/scripts
python filesystem_watcher.py ..

# Terminal 2: Start Orchestrator
cd AI_Employee_Vault/scripts
python orchestrator.py ..
```

**Option 3: Process with Qwen Code**
```bash
cd AI_Employee_Vault
qwen
# Then paste prompt from .qwen_pending.md
```

---

## 📋 Hackathon Tiers

### ✅ Bronze Tier (COMPLETE)
**Time:** 8-12 hours | **Status:** ✅ 21/21 checks passed

- [x] Obsidian vault with Dashboard.md
- [x] Company_Handbook.md with rules
- [x] Business_Goals.md template
- [x] Basic folder structure (Inbox, Needs_Action, Done, etc.)
- [x] One working Watcher (Filesystem)
- [x] Qwen Code integration
- [x] Ralph Wiggum plugin for continuous iteration

### 🔲 Silver Tier (Next Steps)
**Time:** 20-30 hours

- [ ] Gmail Watcher integration
- [ ] WhatsApp Watcher integration
- [ ] MCP server for email sending
- [ ] Approval workflow automation
- [ ] Scheduled tasks (cron/Task Scheduler)

### 🔲 Gold Tier
**Time:** 40+ hours

- [ ] Full cross-domain integration
- [ ] Odoo accounting integration
- [ ] Social media auto-posting
- [ ] Weekly CEO Briefing generation
- [ ] Error recovery and audit logging

### 🔲 Platinum Tier
**Time:** 60+ hours

- [ ] Cloud deployment (24/7 operation)
- [ ] Multi-agent sync
- [ ] Work-zone specialization
- [ ] A2A (Agent-to-Agent) communication

---

## 📂 File Descriptions

### Root Level Files

| File | Purpose |
|------|---------|
| `README.md` | This comprehensive project summary |
| `Personal AI Employee Hackathon 0_...md` | Complete 1201-line architectural blueprint |
| `QWEN.md` | Context file for AI assistants |
| `skills-lock.json` | Tracks installed Qwen skills |
| `verify_bronze_tier.py` | Verification script (21 checks) |

### AI_Employee_Vault Files

| File | Purpose |
|------|---------|
| `Dashboard.md` | Real-time status, metrics, alerts |
| `Company_Handbook.md` | AI employee rules and procedures |
| `Business_Goals.md` | Objectives, targets, subscription list |
| `README.md` | Vault-specific usage instructions |

### Scripts

| File | Purpose |
|------|---------|
| `base_watcher.py` | Abstract base class for all watchers |
| `filesystem_watcher.py` | Monitors Inbox for new files |
| `orchestrator.py` | Triggers Qwen Code on pending items |
| `start_ai_employee.bat` | Windows startup script |
| `ralph_wiggum.py` | Stop hook for continuous iteration |

---

## 🔄 How It Works

### Complete Workflow

```
1. User drops file in Inbox/
        ↓
2. Filesystem Watcher detects new file
        ↓
3. Creates action file in Needs_Action/
        ↓
4. Orchestrator detects pending item
        ↓
5. Creates .qwen_pending.md with prompt
        ↓
6. User runs: qwen
        ↓
7. Qwen reads Company_Handbook.md for rules
        ↓
8. Qwen creates Plan.md for multi-step tasks
        ↓
9. Sensitive actions → Pending_Approval/
        ↓
10. Human moves file to Approved/
        ↓
11. Qwen executes approved action
        ↓
12. Moves completed items to Done/
```

### Example: Processing an Invoice Request

```
📥 Inbox/invoice_request.txt
    ↓
📋 Needs_Action/FILE_invoice_request_2026-03-23.md
    ↓
🤖 Qwen reads and creates plan
    ↓
📝 Plans/Sales_Invoice_Client_10000_Plan.md
    ↓
⏳ Pending_Approval/Invoice_10000_Approval.md
    ↓
✅ Human approves (moves to Approved/)
    ↓
📧 Qwen sends invoice via MCP
    ↓
📊 Logs result in Logs/
    ↓
✅ Moves to Done/
```

---

## 🛠️ Available Skills

### Installed Skills

| Skill | Purpose | Location |
|-------|---------|----------|
| `browsing-with-playwright` | Web automation, form filling, screenshots | `.qwen/skills/browsing-with-playwright/` |

### Skill Capabilities

- Navigate websites
- Fill forms
- Click elements
- Take screenshots
- Extract data
- Execute JavaScript

---

## 📊 Current Status

### Vault Contents (As of analysis)

| Folder | Items | Description |
|--------|-------|-------------|
| `Inbox/` | 7 files | Pending input files |
| `Needs_Action/` | 0 files | Ready for processing |
| `Plans/` | 6 files | Active task plans |
| `Pending_Approval/` | 0 files | Awaiting approval |
| `Approved/` | 10 files | Ready for execution |
| `Done/` | 10 files | Completed tasks |
| `Invoices/` | 3 files | Generated invoices |
| `Logs/` | 5 files | System logs |

### Generated Documents

- **Invoices:** INV-2026-001, INV-2026-002, INV-2026-003
- **Plans:** Invoice plans, Payment receipt plans, Utility bill plans
- **Approvals:** Sales invoices, Utility bills, Payment approvals

---

## 🔧 Configuration

### Python Dependencies

```txt
# requirements.txt
watchdog>=3.0.0
```

### Qwen Code Setup

```bash
# Verify installation
qwen --version

# Expected output: 0.12.6
```

### Obsidian Vault

Open `AI_Employee_Vault/` as a vault in Obsidian:
1. Open Obsidian
2. Click "Open folder as vault"
3. Select `AI_Employee_Vault/`

---

## 📝 Meeting Information

**Weekly Research & Showcase**
- **When:** Wednesdays at 10:00 PM PKT
- **Zoom:** [Join Meeting](https://us06web.zoom.us/j/87188707642?pwd=a9XloCsinvn1JzICbPc2YGUvWTbOTr.1)
- **YouTube:** [@panaversity](https://www.youtube.com/@panaversity)

---

## 🎓 Learning Resources

### Prerequisites (Complete First)

| Topic | Resource | Time |
|-------|----------|------|
| Qwen Code Fundamentals | See QWEN.md | 3 hours |
| Obsidian Fundamentals | help.obsidian.md | 30 min |
| Python File I/O | realpython.com | 1 hour |
| Agent Skills | platform.claude.com/docs | 2 hours |

### Core Learning

| Topic | Resource |
|-------|----------|
| Building MCP Servers | modelcontextprotocol.io/quickstart |
| Playwright Automation | playwright.dev/python |
| Agent Architecture | Anthropic documentation |

---

## 🏆 Judging Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Functionality | 30% | Does it work? Core features complete? |
| Innovation | 25% | Creative solutions, novel integrations |
| Practicality | 20% | Would you actually use this daily? |
| Security | 15% | Proper credential handling, HITL safeguards |
| Documentation | 10% | Clear README, setup instructions, demo |

---

## 📄 License & Credits

**Project:** AI Digital FTEs - Personal AI Employee Hackathon  
**Blueprint:** 1201-line comprehensive architectural guide  
**Implementation:** Bronze Tier Complete  
**AI Engine:** Qwen Code (v0.12.6)  
**Knowledge Base:** Obsidian Markdown  

---

## 🚨 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Watcher not detecting files | Check `Inbox/` exists, view `Logs/` |
| Qwen not found | Run `qwen --version`, reinstall if needed |
| Permission errors | Run terminal as Administrator |
| Orchestrator timeout | Normal - runs continuously until stopped |

### Getting Help

1. Check logs in `AI_Employee_Vault/Logs/`
2. Review `Company_Handbook.md` for rules
3. Run verification: `python verify_bronze_tier.py AI_Employee_Vault`
4. Join Wednesday meetings for support

---

## 📈 Next Steps

1. **Test the system:** Drop a file in `Inbox/` and process it
2. **Customize handbook:** Edit `Company_Handbook.md` with your rules
3. **Set goals:** Update `Business_Goals.md` with your targets
4. **Upgrade to Silver:** Add Gmail/WhatsApp watchers
5. **Deploy:** Consider Platinum tier for 24/7 cloud operation

---

*AI Employee v0.1 (Bronze Tier) - Built with Qwen Code & Obsidian*  
*Last Updated: March 23, 2026*
