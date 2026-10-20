# DevPulse AI - Autonomous AI Software Engineering Agent & Cloud IDE

A modern, full-stack AI Software Engineering Agent and Cloud IDE featuring an autonomous agent builder, conversational coding chatbot, Monaco code editor, live multi-runtime execution engine, automated AI debugger, and live web application preview.

---

## 🌟 Key Features

### 1. 🤖 Autonomous AI Agent (Builder Mode)
- **Goal-Driven Planning**: Provide any high-level objective (e.g. *"Build an interactive Weather Dashboard"*, *"Create a Scientific Calculator"*, *"Write a REST API with FastAPI"*).
- **Task Decomposition**: Automatically generates multi-step implementation milestones.
- **Autonomous Workspace Artifact Generation**: Writes, modifies, and organizes production-grade code across files and directories.
- **One-Click Workspace Sync**: Immediate navigation to newly generated artifacts.

### 2. 💬 AI Engineering Chatbot (Q&A Mode)
- **Context-Aware Software Engineer**: Ask any programming question, algorithm design, architecture trade-offs, performance optimizations, or framework guidance.
- **Support for Frontier LLMs & Local Mode**:
  - **Google Gemini** (gemini-2.5-flash, gemini-2.0-flash, gemini-1.5-pro)
  - **OpenAI** (gpt-4o, gpt-4o-mini)
  - **Groq** (llama-3.3-70b-versatile)
  - **Ollama** (local offline models)
  - **DevPulse Offline Engine** (zero keys required out-of-the-box!)

### 3. 💻 Monaco Code Editor (VS Code Experience)
- Full **Monaco Editor** integration with syntax highlighting for 50+ languages (Python, JavaScript, TypeScript, HTML, CSS, JSON, Shell, Markdown).
- **Multi-Tab File Management**: Open, switch, and close multiple files with unsaved change indicators (`•`).
- **Direct AI Shortcuts**:
  - 📖 **Explain Code**: Instant breakdown of time/space complexity and algorithms.
  - ✨ **Refactor**: Rewrite code for performance and idiomatic best practices.
  - 🧪 **Generate Tests**: Create comprehensive unit tests with edge cases.
- Keyboard shortcuts: `Ctrl+S` (Save file), `Ctrl+Enter` (Run code).

### 4. ▶️ Multi-Language Execution Engine & Terminal
- **Python Runtime**: Executes Python scripts with isolated stdout/stderr capture, execution timing, and return codes.
- **Node.js Runtime**: Executes JavaScript and asynchronous pipelines directly.
- **Interactive Terminal**: Run workspace shell/powershell commands (`dir`, `python --version`, `pip list`).

### 5. 🐞 Automated AI Debugger & One-Click Patching
- When a script encounters an exception or traceback, the **AI Debugger** activates.
- **Root Cause Analysis**: Explains the exact failure mechanism and line location.
- **Diagnosis**: Clear natural language architectural explanation.
- **1-Click "Apply Fix to Editor"**: Instantly patches the code in the editor and saves the file.

### 6. 🌐 Live Web Preview
- Dedicated live preview tab for web applications (`HTML`/`CSS`/`JavaScript`).
- Includes built-in address bar, refresh button, and open in external tab.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+ (optional, already pre-built in `frontend/dist`)

### Quick Start (1 Command)
```bash
python run.py
```
Open **[http://localhost:8000](http://localhost:8000)** in your browser!

---

## ⚙️ Configuration & Settings
Click the **Settings** gear icon in the top right of the IDE to configure:
- **Provider**: Google Gemini / OpenAI / Groq / Ollama / Local Built-in.
- **API Key**: Enter your key (e.g. Gemini API Key from Google AI Studio).
- **Model Name**: Select or customize model string.

---

## 📁 Project Structure

```
software_engineer_agent/
├── backend/
│   ├── config.py             # Workspace & Provider settings
│   ├── workspace_manager.py  # File tree, CRUD, ZIP export, samples
│   ├── execution_engine.py   # Python, Node.js, and Shell runners
│   ├── ai_engine.py          # Gemini, OpenAI, Groq, Agent planner, Debugger
│   └── main.py               # FastAPI REST endpoints & static hosting
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.jsx        # File tree explorer & quick demos
│   │   │   ├── AIPanel.jsx        # Chatbot Q&A & Autonomous Agent tabs
│   │   │   ├── EditorArea.jsx     # Monaco editor with tabs & AI actions
│   │   │   ├── ConsoleOutput.jsx  # Execution terminal & AI debugger
│   │   │   ├── WebPreview.jsx     # Live HTML/CSS/JS web preview
│   │   │   └── SettingsModal.jsx  # Provider & API key configuration
│   │   ├── services/api.js        # Frontend-backend API service
│   │   ├── App.jsx                # Unified application orchestrator
│   │   └── index.css              # Modern dark theme styles
│   ├── dist/                      # Production-ready compiled assets
│   └── vite.config.js             # Vite configuration with proxy
├── workspace/                     # User workspace where code is built & run
├── run.py                         # Single-command launcher
└── test_system.py                 # Automated verification test suite
```
