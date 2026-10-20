import os
from pathlib import Path
from fastapi import FastAPI, HTTPException, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

from .config import CURRENT_SETTINGS, WORKSPACE_DIR, Settings, save_persisted_settings
from .workspace_manager import (
    list_workspace_tree,
    read_workspace_file,
    write_workspace_file,
    delete_workspace_item,
    rename_workspace_item,
    create_workspace_folder,
    export_workspace_zip,
    seed_sample_projects,
    get_safe_path
)
from .execution_engine import execute_code, execute_terminal_command
from .ai_engine import (
    call_llm,
    run_autonomous_agent,
    debug_code_error,
    perform_quick_action
)

# Seed starter projects
seed_sample_projects()

app = FastAPI(title="DevPulse AI Agent API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# Request Models
# -------------------------------------------------------------
class FileWriteRequest(BaseModel):
    path: str
    content: str

class FolderCreateRequest(BaseModel):
    path: str

class RenameRequest(BaseModel):
    old_path: str
    new_path: str

class ExecuteRequest(BaseModel):
    code: str
    language: str
    file_path: Optional[str] = None

class TerminalRequest(BaseModel):
    command: str

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

class AgentTaskRequest(BaseModel):
    task: str
    context_files: Optional[List[str]] = None

class DebugRequest(BaseModel):
    file_path: str
    code: str
    error_message: str

class QuickActionRequest(BaseModel):
    action: str
    code: str
    language: str

# -------------------------------------------------------------
# Workspace Endpoints
# -------------------------------------------------------------
@app.get("/api/workspace/tree")
async def get_tree():
    return {"tree": list_workspace_tree()}

@app.get("/api/workspace/file")
async def get_file(path: str = Query(...)):
    try:
        return read_workspace_file(path)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/workspace/file")
async def save_file(req: FileWriteRequest):
    try:
        return write_workspace_file(req.path, req.content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/workspace/file")
async def delete_file(path: str = Query(...)):
    try:
        return delete_workspace_item(path)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/workspace/folder")
async def create_folder(req: FolderCreateRequest):
    try:
        return create_workspace_folder(req.path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/workspace/rename")
async def rename_item(req: RenameRequest):
    try:
        return rename_workspace_item(req.old_path, req.new_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/workspace/download")
async def download_zip():
    buf = export_workspace_zip()
    return StreamingResponse(
        buf,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=devpulse_workspace.zip"}
    )

@app.post("/api/workspace/reset-samples")
async def reset_samples():
    seed_sample_projects()
    return {"message": "Workspace initialized with sample projects", "tree": list_workspace_tree()}

# -------------------------------------------------------------
# Code Execution & Terminal Endpoints
# -------------------------------------------------------------
@app.post("/api/execute")
async def run_code_endpoint(req: ExecuteRequest):
    result = execute_code(code=req.code, language=req.language, file_path=req.file_path)
    return result

@app.post("/api/terminal")
async def run_terminal_endpoint(req: TerminalRequest):
    result = execute_terminal_command(req.command)
    return result

# -------------------------------------------------------------
# AI Intelligence Endpoints
# -------------------------------------------------------------
@app.post("/api/ai/chat")
async def chat_endpoint(req: ChatRequest):
    msgs = [{"role": m.role, "content": m.content} for m in req.messages]
    response_text = await call_llm(msgs)
    return {"reply": response_text}

@app.post("/api/ai/agent")
async def agent_task_endpoint(req: AgentTaskRequest):
    plan_result = await run_autonomous_agent(req.task, req.context_files)
    return plan_result

@app.post("/api/ai/debug")
async def debug_endpoint(req: DebugRequest):
    analysis = await debug_code_error(req.file_path, req.code, req.error_message)
    return analysis

@app.post("/api/ai/quick-action")
async def quick_action_endpoint(req: QuickActionRequest):
    result = await perform_quick_action(req.action, req.code, req.language)
    return result

# -------------------------------------------------------------
# Settings Endpoints
# -------------------------------------------------------------
@app.get("/api/settings")
async def get_settings():
    return {
        "provider": CURRENT_SETTINGS.provider,
        "model_name": CURRENT_SETTINGS.model_name,
        "has_gemini_key": bool(CURRENT_SETTINGS.gemini_api_key),
        "has_openai_key": bool(CURRENT_SETTINGS.openai_api_key),
        "has_groq_key": bool(CURRENT_SETTINGS.groq_api_key),
        "ollama_base_url": CURRENT_SETTINGS.ollama_base_url
    }

@app.post("/api/settings")
async def update_settings(new_settings: Settings):
    CURRENT_SETTINGS.provider = new_settings.provider
    if new_settings.gemini_api_key is not None:
        CURRENT_SETTINGS.gemini_api_key = new_settings.gemini_api_key
    if new_settings.openai_api_key is not None:
        CURRENT_SETTINGS.openai_api_key = new_settings.openai_api_key
    if new_settings.groq_api_key is not None:
        CURRENT_SETTINGS.groq_api_key = new_settings.groq_api_key
    if new_settings.ollama_base_url:
        CURRENT_SETTINGS.ollama_base_url = new_settings.ollama_base_url
    if new_settings.model_name:
        CURRENT_SETTINGS.model_name = new_settings.model_name
    save_persisted_settings(CURRENT_SETTINGS)
    return {"message": "Settings updated successfully"}

# -------------------------------------------------------------
# Serve Workspace files for Live Preview (HTML/CSS/JS)
# -------------------------------------------------------------
@app.get("/workspace-preview/{subpath:path}")
async def preview_workspace_file(subpath: str):
    target = get_safe_path(subpath)
    if not target.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(str(target))

# Mount Frontend static build if exists
FRONTEND_DIST = Path(__file__).resolve().parent.parent / "frontend" / "dist"
if FRONTEND_DIST.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIST), html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
