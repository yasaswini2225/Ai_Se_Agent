import subprocess
import os
import time
import sys
import shutil
from pathlib import Path
from typing import Dict, Any, Optional
from .config import WORKSPACE_DIR

def get_node_executable() -> Optional[str]:
    return shutil.which("node")

def execute_code(
    code: str,
    language: str,
    file_path: Optional[str] = None,
    timeout_sec: float = 12.0
) -> Dict[str, Any]:
    """
    Executes code in the specified language (python, javascript/node, or bash/shell).
    If file_path is given, executes the saved file; otherwise creates a temporary script in workspace.
    """
    start_time = time.perf_counter()
    temp_file: Optional[Path] = None

    try:
        # Determine execution path
        if file_path:
            clean_path = file_path.lstrip("/\\")
            exec_target = (WORKSPACE_DIR / clean_path).resolve()
            if code:
                exec_target.write_text(code, encoding="utf-8")
        else:
            ext = ".py" if language.lower() in ("python", "py") else (".js" if language.lower() in ("javascript", "js", "node") else ".txt")
            temp_file = WORKSPACE_DIR / f"_temp_run_{int(time.time() * 1000)}{ext}"
            temp_file.write_text(code, encoding="utf-8")
            exec_target = temp_file

        lang = language.lower()

        if lang in ("python", "py"):
            cmd = [sys.executable, str(exec_target)]
        elif lang in ("javascript", "js", "node"):
            node_exe = get_node_executable()
            if not node_exe:
                return {
                    "stdout": "",
                    "stderr": "Node.js executable was not found on system PATH.",
                    "exit_code": 1,
                    "execution_time_ms": 0,
                    "status": "error",
                    "language": language
                }
            cmd = [node_exe, str(exec_target)]
        elif lang in ("html", "css"):
            # HTML is rendered via client-side preview, but we can acknowledge it
            return {
                "stdout": f"Preview HTML rendered via Live Web Preview tab ({exec_target.name}).",
                "stderr": "",
                "exit_code": 0,
                "execution_time_ms": 1,
                "status": "success",
                "language": language
            }
        else:
            return {
                "stdout": "",
                "stderr": f"Direct execution for language '{language}' is not configured. Supported: python, javascript/node.",
                "exit_code": 1,
                "execution_time_ms": 0,
                "status": "error",
                "language": language
            }

        # Prepare UTF-8 environment for Python and subprocesses on Windows
        sub_env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}

        # Run subprocess with timeout
        proc = subprocess.run(
            cmd,
            cwd=str(WORKSPACE_DIR),
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            encoding="utf-8",
            errors="replace",
            env=sub_env
        )

        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        has_error = proc.returncode != 0

        return {
            "stdout": proc.stdout or "",
            "stderr": proc.stderr or "",
            "exit_code": proc.returncode,
            "execution_time_ms": elapsed_ms,
            "status": "error" if has_error else "success",
            "language": language
        }

    except subprocess.TimeoutExpired:
        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        return {
            "stdout": "",
            "stderr": f"Execution timed out after {timeout_sec} seconds. Check for infinite loops or blocking calls.",
            "exit_code": -1,
            "execution_time_ms": elapsed_ms,
            "status": "timeout",
            "language": language
        }
    except Exception as e:
        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        return {
            "stdout": "",
            "stderr": f"Execution failure: {str(e)}",
            "exit_code": 1,
            "execution_time_ms": elapsed_ms,
            "status": "error",
            "language": language
        }
    finally:
        # Cleanup temporary execution file
        if temp_file and temp_file.exists():
            try:
                temp_file.unlink()
            except Exception:
                pass

def execute_terminal_command(command: str, timeout_sec: float = 15.0) -> Dict[str, Any]:
    """Execute arbitrary shell/powershell commands inside the workspace directory."""
    start_time = time.perf_counter()
    try:
        sub_env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
        proc = subprocess.run(
            ["powershell", "-Command", command],
            cwd=str(WORKSPACE_DIR),
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            encoding="utf-8",
            errors="replace",
            env=sub_env
        )
        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        return {
            "stdout": proc.stdout or "",
            "stderr": proc.stderr or "",
            "exit_code": proc.returncode,
            "execution_time_ms": elapsed_ms,
            "status": "error" if proc.returncode != 0 else "success"
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": f"Command timed out after {timeout_sec}s.",
            "exit_code": -1,
            "execution_time_ms": round((time.perf_counter() - start_time) * 1000, 2),
            "status": "timeout"
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": 1,
            "execution_time_ms": 0,
            "status": "error"
        }
