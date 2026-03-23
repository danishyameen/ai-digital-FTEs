# AI Digital FTEs - Project Context

## Project Overview

This repository contains the blueprint and resources for building **Personal AI Employees** (Digital FTEs - Full-Time Equivalents). It is a documentation-focused project for a hackathon that teaches participants how to create autonomous AI agents that manage personal and business affairs 24/7.

**Core Concept:** Build an AI agent that works like a human employee but with:
- 168 hours/week availability (vs 40 hours for humans)
- 85-90% cost reduction per task
- Instant scaling and consistency

## Repository Contents

### Key Files

| File | Purpose |
|------|---------|
| `Personal AI Employee Hackathon 0_ Building Autonomous FTEs in 2026.md` | Main hackathon blueprint (1201 lines) - comprehensive architectural guide |
| `skills-lock.json` | Tracks installed Qwen skills and their versions |
| `QWEN.md` | This context file for AI assistants |

### Directory Structure

```
ai-digital-FTEs/
├── .qwen/skills/           # Qwen skill configurations
│   └── browsing-with-playwright/
├── .git/                   # Git version control
└── Documentation files
```

## Architecture Summary (From Hackathon Blueprint)

The AI Employee architecture consists of:

### 1. The Foundational Layer (Local Engine)
- **Obsidian:** Acts as GUI and Long-Term Memory (Dashboard.md, Company_Handbook.md)
- **Claude Code:** Primary reasoning engine running in terminal

### 2. Perception → Reasoning → Action

| Layer | Component | Purpose |
|-------|-----------|---------|
| **Perception** | Python Watcher Scripts | Monitor Gmail, WhatsApp, filesystems |
| **Reasoning** | Claude Code | Creates Plan.md files, makes decisions |
| **Action** | MCP Servers | Execute external actions (email, browser, payments) |

### 3. Key Patterns

- **Watcher Pattern:** Lightweight Python scripts that monitor inputs and create `.md` files in `/Needs_Action` folders
- **Ralph Wiggum Loop:** Stop hook pattern that keeps Claude iterating until tasks are complete
- **Human-in-the-Loop:** Sensitive actions require approval via file movement (`/Pending_Approval` → `/Approved`)

## Hackathon Tiers

| Tier | Time Estimate | Deliverables |
|------|---------------|--------------|
| **Bronze** | 8-12 hours | Obsidian vault, 1 Watcher, basic folder structure |
| **Silver** | 20-30 hours | Multiple Watchers, MCP server, approval workflow |
| **Gold** | 40+ hours | Full integration, Odoo accounting, weekly briefings |
| **Platinum** | 60+ hours | Cloud deployment, 24/7 operation, multi-agent sync |

## Usage Guidelines

### For AI Assistants

When working in this repository:

1. **Primary Reference:** The hackathon blueprint document contains all architectural details
2. **Skill Usage:** The `browsing-with-playwright` skill is available for web automation tasks
3. **Folder Conventions:**
   - `/Inbox` - Raw incoming items
   - `/Needs_Action` - Items requiring processing
   - `/Done` - Completed items
   - `/Pending_Approval` - Awaiting human approval
   - `/Approved` - Ready for execution

### Common Tasks

- **Adding new skills:** Place in `.qwen/skills/` with `SKILL.md` documentation
- **Creating watchers:** Follow the base watcher pattern from the blueprint
- **MCP integration:** Configure in Claude Code settings per blueprint examples

## Meeting Information

**Weekly Research & Showcase:** Wednesdays at 10:00 PM PKT
- Zoom: https://us06web.zoom.us/j/87188707642?pwd=a9XloCsinvn1JzICbPc2YGUvWTbOTr.1
- YouTube: https://www.youtube.com/@panaversity

## Prerequisites (From Blueprint)

| Component | Version | Purpose |
|-----------|---------|---------|
| Claude Code | Active subscription | Reasoning engine |
| Obsidian | v1.10.6+ | Knowledge base & dashboard |
| Python | 3.13+ | Watcher scripts |
| Node.js | v24+ LTS | MCP servers |
| GitHub Desktop | Latest | Version control |

## Notes for AI Assistants

- This is a **documentation/knowledge project**, not a traditional code repository
- The main artifact is the hackathon blueprint markdown file
- When users ask about implementation, refer them to the detailed blueprint document
- The project emphasizes **local-first**, **privacy-focused** AI automation
- All AI functionality should be implemented as [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
