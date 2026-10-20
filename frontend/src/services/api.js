const API_BASE = '/api';

export const api = {
  // Workspace
  async getTree() {
    const res = await fetch(`${API_BASE}/workspace/tree`);
    if (!res.ok) throw new Error('Failed to fetch workspace tree');
    return res.json();
  },

  async getFile(path) {
    const res = await fetch(`${API_BASE}/workspace/file?path=${encodeURIComponent(path)}`);
    if (!res.ok) throw new Error('Failed to read file');
    return res.json();
  },

  async saveFile(path, content) {
    const res = await fetch(`${API_BASE}/workspace/file`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path, content })
    });
    if (!res.ok) throw new Error('Failed to save file');
    return res.json();
  },

  async deleteItem(path) {
    const res = await fetch(`${API_BASE}/workspace/file?path=${encodeURIComponent(path)}`, {
      method: 'DELETE'
    });
    if (!res.ok) throw new Error('Failed to delete item');
    return res.json();
  },

  async createFolder(path) {
    const res = await fetch(`${API_BASE}/workspace/folder`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path })
    });
    if (!res.ok) throw new Error('Failed to create folder');
    return res.json();
  },

  async renameItem(oldPath, newPath) {
    const res = await fetch(`${API_BASE}/workspace/rename`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ old_path: oldPath, new_path: newPath })
    });
    if (!res.ok) throw new Error('Failed to rename item');
    return res.json();
  },

  async resetSamples() {
    const res = await fetch(`${API_BASE}/workspace/reset-samples`, { method: 'POST' });
    if (!res.ok) throw new Error('Failed to reset workspace');
    return res.json();
  },

  downloadZipUrl() {
    return `${API_BASE}/workspace/download`;
  },

  // Execution
  async executeCode(code, language, filePath) {
    const res = await fetch(`${API_BASE}/execute`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, language, file_path: filePath })
    });
    if (!res.ok) throw new Error('Code execution failed');
    return res.json();
  },

  async executeTerminal(command) {
    const res = await fetch(`${API_BASE}/terminal`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ command })
    });
    if (!res.ok) throw new Error('Terminal execution failed');
    return res.json();
  },

  // AI Intelligence
  async sendChat(messages) {
    const res = await fetch(`${API_BASE}/ai/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages })
    });
    if (!res.ok) throw new Error('AI Chat failed');
    return res.json();
  },

  async runAgentTask(task, contextFiles = []) {
    const res = await fetch(`${API_BASE}/ai/agent`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task, context_files: contextFiles })
    });
    if (!res.ok) throw new Error('Agent execution failed');
    return res.json();
  },

  async debugCode(filePath, code, errorMessage) {
    const res = await fetch(`${API_BASE}/ai/debug`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ file_path: filePath, code, error_message: errorMessage })
    });
    if (!res.ok) throw new Error('Debugging analysis failed');
    return res.json();
  },

  async quickAction(action, code, language) {
    const res = await fetch(`${API_BASE}/ai/quick-action`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action, code, language })
    });
    if (!res.ok) throw new Error('Quick action failed');
    return res.json();
  },

  // Settings
  async getSettings() {
    const res = await fetch(`${API_BASE}/settings`);
    if (!res.ok) throw new Error('Failed to load settings');
    return res.json();
  },

  async updateSettings(settings) {
    const res = await fetch(`${API_BASE}/settings`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(settings)
    });
    if (!res.ok) throw new Error('Failed to save settings');
    return res.json();
  }
};
