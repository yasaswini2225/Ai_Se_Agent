import os
import sys
from pathlib import Path

# Force UTF-8 encoding for standard outputs on Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import uvicorn

def main():
    print("=" * 65)
    print("  [*] DevPulse AI - AI Software Engineering Agent & IDE")
    print("=" * 65)
    print("  - Autonomous Agent Task Builder")
    print("  - Intelligent Software Engineering Chatbot")
    print("  - Full Monaco Code Editor with Multi-Tabs & Auto-Save")
    print("  - Direct Python, Node.js & Shell Execution Engine")
    print("  - Automated AI Error Diagnosis & One-Click Patching")
    print("  - Live Interactive Web App Preview")
    print("-" * 65)
    print("  Starting DevPulse AI server on: http://localhost:8000")
    print("=" * 65)

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    main()
