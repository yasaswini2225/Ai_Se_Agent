import React, { useState, useEffect } from 'react';
import { 
  Code, Play, Bug, Download, Settings as SettingsIcon, Globe, Layout, 
  Terminal, Sparkles, FolderTree, RefreshCw, PanelLeftClose, PanelLeft,
  ChevronDown, Cpu, Wand2, Check
} from 'lucide-react';

import Sidebar from './components/Sidebar';
import AIPanel from './components/AIPanel';
import EditorArea from './components/EditorArea';
import ConsoleOutput from './components/ConsoleOutput';
import WebPreview from './components/WebPreview';
import SettingsModal from './components/SettingsModal';
import { api } from './services/api';

export default function App() {
  // Navigation / View modes: 'editor' | 'preview'
  const [viewMode, setViewMode] = useState('editor');
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [aiPanelOpen, setAiPanelOpen] = useState(true);
  const [settingsOpen, setSettingsOpen] = useState(false);

  // Workspace & Files
  const [tree, setTree] = useState([]);
  const [openTabs, setOpenTabs] = useState(['analytics.py']);
  const [activeFile, setActiveFile] = useState('analytics.py');
  const [fileContents, setFileContents] = useState({});
  const [dirtyFiles, setDirtyFiles] = useState({});

  // Execution & Debugging
  const [output, setOutput] = useState(null);
  const [isExecuting, setIsExecuting] = useState(false);
  const [debugResult, setDebugResult] = useState(null);
  const [isDebugging, setIsDebugging] = useState(false);
  const [quickActionResult, setQuickActionResult] = useState(null);
  const [isQuickActionLoading, setIsQuickActionLoading] = useState(false);
  const [activeConsoleTab, setActiveConsoleTab] = useState('output');

  // Initial load
  useEffect(() => {
    loadWorkspace();
    loadFileContent('analytics.py');
  }, []);

  const loadWorkspace = async () => {
    try {
      const data = await api.getTree();
      setTree(data.tree || []);
    } catch (err) {
      console.error('Failed to load workspace tree:', err);
    }
  };

  const loadFileContent = async (path) => {
    if (!path) return;
    try {
      const data = await api.getFile(path);
      setFileContents(prev => ({ ...prev, [path]: data.content }));
      // Ensure tab is open
      setOpenTabs(prev => prev.includes(path) ? prev : [...prev, path]);
      setActiveFile(path);
    } catch (err) {
      console.error(`Failed to load file ${path}:`, err);
    }
  };

  const handleSelectFile = (path) => {
    loadFileContent(path);
    // If opening an html file and in preview mode, keep preview, else if in preview switch or keep
  };

  const handleCloseTab = (path) => {
    const nextTabs = openTabs.filter(p => p !== path);
    setOpenTabs(nextTabs);
    if (activeFile === path) {
      setActiveFile(nextTabs.length > 0 ? nextTabs[nextTabs.length - 1] : null);
    }
    // Clean dirty state if closed
    setDirtyFiles(prev => {
      const copy = { ...prev };
      delete copy[path];
      return copy;
    });
  };

  const handleContentChange = (path, newContent) => {
    setFileContents(prev => ({ ...prev, [path]: newContent }));
    setDirtyFiles(prev => ({ ...prev, [path]: true }));
  };

  const handleSaveFile = async (path) => {
    const content = fileContents[path];
    if (content === undefined) return;
    try {
      await api.saveFile(path, content);
      setDirtyFiles(prev => {
        const copy = { ...prev };
        delete copy[path];
        return copy;
      });
    } catch (err) {
      alert(`Save error: ${err.message}`);
    }
  };

  const handleCreateFile = async (relPath) => {
    try {
      await api.saveFile(relPath, '');
      await loadWorkspace();
      loadFileContent(relPath);
    } catch (err) {
      alert(`Error creating file: ${err.message}`);
    }
  };

  const handleCreateFolder = async (relPath) => {
    try {
      await api.createFolder(relPath);
      await loadWorkspace();
    } catch (err) {
      alert(`Error creating folder: ${err.message}`);
    }
  };

  const handleDeleteItem = async (relPath) => {
    try {
      await api.deleteItem(relPath);
      handleCloseTab(relPath);
      await loadWorkspace();
    } catch (err) {
      alert(`Error deleting item: ${err.message}`);
    }
  };

  const handleRenameItem = async (oldPath, newPath) => {
    try {
      await api.renameItem(oldPath, newPath);
      handleCloseTab(oldPath);
      await loadWorkspace();
      loadFileContent(newPath);
    } catch (err) {
      alert(`Error renaming item: ${err.message}`);
    }
  };

  const handleResetSamples = async () => {
    try {
      await api.resetSamples();
      await loadWorkspace();
      loadFileContent('analytics.py');
    } catch (err) {
      alert(`Failed to load samples: ${err.message}`);
    }
  };

  // Execution
  const handleRunCode = async () => {
    if (!activeFile) return;
    
    // Auto-save before running
    if (dirtyFiles[activeFile]) {
      await handleSaveFile(activeFile);
    }

    const content = fileContents[activeFile] ?? '';
    const ext = activeFile.split('.').pop().toLowerCase();
    
    // If it's HTML, switch to live preview tab!
    if (ext === 'html') {
      setViewMode('preview');
      return;
    }

    const language = ext === 'py' ? 'python' : (['js', 'jsx', 'ts'].includes(ext) ? 'javascript' : ext);
    setIsExecuting(true);
    setActiveConsoleTab('output');
    setViewMode('editor');

    try {
      const res = await api.executeCode(content, language, activeFile);
      setOutput(res);
      // If error occurred, automatically prepare debugging session
      if (res.status === 'error') {
        setDebugResult(null);
      }
    } catch (err) {
      setOutput({
        stdout: '',
        stderr: err.message,
        exit_code: 1,
        execution_time_ms: 0,
        status: 'error'
      });
    } finally {
      setIsExecuting(false);
    }
  };

  // Debugging
  const handleTriggerDebug = async () => {
    if (!activeFile || !output || !output.stderr) return;
    setIsDebugging(true);
    setActiveConsoleTab('debug');
    try {
      const res = await api.debugCode(activeFile, fileContents[activeFile] || '', output.stderr);
      setDebugResult(res);
    } catch (err) {
      setDebugResult({
        root_cause: 'Diagnostic request error',
        diagnosis: err.message,
        fixed_code: null
      });
    } finally {
      setIsDebugging(false);
    }
  };

  const handleApplyFix = async (fixedCode) => {
    if (!activeFile || !fixedCode) return;
    setFileContents(prev => ({ ...prev, [activeFile]: fixedCode }));
    await api.saveFile(activeFile, fixedCode);
    setDirtyFiles(prev => {
      const copy = { ...prev };
      delete copy[activeFile];
      return copy;
    });
    // Auto re-run to confirm fix
    setOutput(null);
    setDebugResult(null);
    setActiveConsoleTab('output');
    setTimeout(() => {
      handleRunCode();
    }, 200);
  };

  // Quick Action
  const handleQuickAction = async (action) => {
    if (!activeFile) return;
    const content = fileContents[activeFile] || '';
    const ext = activeFile.split('.').pop().toLowerCase();
    const language = ext === 'py' ? 'python' : (ext === 'js' ? 'javascript' : ext);

    setIsQuickActionLoading(true);
    setActiveConsoleTab('quickAction');

    try {
      const res = await api.quickAction(action, content, language);
      setQuickActionResult(res);
    } catch (err) {
      setQuickActionResult({
        action,
        summary: `Error running ${action}: ${err.message}`,
        markdown: `Error: ${err.message}`,
        code: null
      });
    } finally {
      setIsQuickActionLoading(false);
    }
  };

  const handleApplyRefactor = async (newCode) => {
    if (!activeFile || !newCode) return;
    setFileContents(prev => ({ ...prev, [activeFile]: newCode }));
    await api.saveFile(activeFile, newCode);
    setDirtyFiles(prev => {
      const copy = { ...prev };
      delete copy[activeFile];
      return copy;
    });
    alert('Refactored code applied and saved successfully!');
  };

  const handleSaveAsTestFile = async (testCode) => {
    if (!activeFile || !testCode) return;
    const parts = activeFile.split('/');
    const fileName = parts.pop();
    const testFileName = fileName.startsWith('test_') ? fileName : `test_${fileName}`;
    const testPath = parts.length > 0 ? `${parts.join('/')}/${testFileName}` : testFileName;

    await api.saveFile(testPath, testCode);
    await loadWorkspace();
    loadFileContent(testPath);
    alert(`Unit test suite saved to '${testPath}' and opened in Editor!`);
  };

  const handleInsertCode = (code) => {
    if (!activeFile) return;
    const current = fileContents[activeFile] || '';
    const updated = current ? `${current}\n\n${code}` : code;
    handleContentChange(activeFile, updated);
  };

  return (
    <div className="flex flex-col h-screen w-screen bg-[#0d0f17] text-slate-100 overflow-hidden font-sans">
      {/* Top Application Header */}
      <header className="h-12 border-b border-slate-800 bg-slate-950/90 px-4 flex items-center justify-between select-none">
        {/* Brand & Left Toggles */}
        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-2">
            <div className="relative flex items-center justify-center w-7 h-7 rounded-lg bg-gradient-to-tr from-indigo-600 to-sky-500 shadow-lg shadow-indigo-500/30">
              <Sparkles className="w-4 h-4 text-white" />
              <span className="absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-emerald-400 ring-2 ring-slate-950 animate-pulse" />
            </div>
            <div>
              <div className="flex items-center space-x-1.5">
                <span className="font-bold text-sm tracking-tight text-white">DevPulse</span>
                <span className="text-[10px] font-mono px-1.5 py-0.2 bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 rounded">
                  AI AGENT IDE
                </span>
              </div>
            </div>
          </div>

          <div className="h-4 w-px bg-slate-800 mx-1" />

          {/* Toggle Panels Buttons */}
          <button
            onClick={() => setSidebarOpen(v => !v)}
            title="Toggle File Explorer"
            className={`p-1.5 rounded-lg border transition ${
              sidebarOpen 
                ? 'bg-slate-800 text-indigo-400 border-slate-700' 
                : 'bg-slate-950 text-slate-500 hover:text-slate-200 border-slate-800'
            }`}
          >
            <FolderTree className="w-3.5 h-3.5" />
          </button>

          <button
            onClick={() => setAiPanelOpen(v => !v)}
            title="Toggle AI Agent Panel"
            className={`p-1.5 rounded-lg border transition ${
              aiPanelOpen 
                ? 'bg-slate-800 text-indigo-400 border-slate-700' 
                : 'bg-slate-950 text-slate-500 hover:text-slate-200 border-slate-800'
            }`}
          >
            <Cpu className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Center: View Switcher (Code Editor vs Live Web Preview) */}
        <div className="flex bg-slate-900 border border-slate-800 p-0.5 rounded-xl text-xs">
          <button
            onClick={() => setViewMode('editor')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded-lg transition font-medium ${
              viewMode === 'editor'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Code className="w-3.5 h-3.5" />
            <span>Code Editor</span>
          </button>
          <button
            onClick={() => setViewMode('preview')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded-lg transition font-medium ${
              viewMode === 'preview'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Globe className="w-3.5 h-3.5" />
            <span>Live Web Preview</span>
          </button>
        </div>

        {/* Right Header Utilities: Run, Debug, Export, Settings */}
        <div className="flex items-center space-x-2">
          {/* Run Code */}
          <button
            onClick={handleRunCode}
            disabled={isExecuting || !activeFile}
            className="flex items-center space-x-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 disabled:bg-slate-800 text-white rounded-lg text-xs font-semibold shadow-md shadow-emerald-900/20 transition"
          >
            {isExecuting ? (
              <div className="w-3 h-3 border-2 border-white border-t-transparent rounded-full animate-spin" />
            ) : (
              <Play className="w-3 h-3 fill-white" />
            )}
            <span>Run Code</span>
          </button>

          {/* Debug with AI */}
          {output && output.status === 'error' && (
            <button
              onClick={handleTriggerDebug}
              disabled={isDebugging}
              className="flex items-center space-x-1.5 px-3 py-1.5 bg-gradient-to-r from-rose-600 to-indigo-600 hover:from-rose-500 hover:to-indigo-500 text-white rounded-lg text-xs font-semibold shadow-md transition animate-pulse"
            >
              <Wand2 className="w-3.5 h-3.5" />
              <span>Debug with AI</span>
            </button>
          )}

          {/* Download Workspace as ZIP */}
          <a
            href={api.downloadZipUrl()}
            download
            title="Download Workspace as ZIP"
            className="p-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-800 rounded-lg transition"
          >
            <Download className="w-3.5 h-3.5" />
          </a>

          {/* Settings */}
          <button
            onClick={() => setSettingsOpen(true)}
            title="Configure AI Models & Keys"
            className="p-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-800 rounded-lg transition"
          >
            <SettingsIcon className="w-3.5 h-3.5" />
          </button>
        </div>
      </header>

      {/* Main App Workspace Layout */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left: Workspace Tree Sidebar */}
        {sidebarOpen && (
          <Sidebar
            tree={tree}
            activeFile={activeFile}
            onSelectFile={handleSelectFile}
            onRefreshTree={loadWorkspace}
            onCreateFile={handleCreateFile}
            onCreateFolder={handleCreateFolder}
            onDeleteItem={handleDeleteItem}
            onRenameItem={handleRenameItem}
            onResetSamples={handleResetSamples}
          />
        )}

        {/* Second Column: AI Agent & Chatbot Assistant */}
        {aiPanelOpen && (
          <AIPanel
            activeFile={activeFile}
            onOpenFile={handleSelectFile}
            onRefreshWorkspace={loadWorkspace}
            onNavigateToPreview={() => setViewMode('preview')}
            onInsertCode={handleInsertCode}
          />
        )}

        {/* Main Center Stage: Editor Area OR Live Web Preview */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {viewMode === 'editor' ? (
            <>
              {/* Monaco Code Editor */}
              <EditorArea
                openTabs={openTabs}
                activeFile={activeFile}
                fileContents={fileContents}
                dirtyFiles={dirtyFiles}
                onSelectTab={setActiveFile}
                onCloseTab={handleCloseTab}
                onContentChange={handleContentChange}
                onSaveFile={handleSaveFile}
                onRunCode={handleRunCode}
                onTriggerDebug={handleTriggerDebug}
                onQuickAction={handleQuickAction}
                isExecuting={isExecuting}
                isQuickActionLoading={isQuickActionLoading}
              />

              {/* Console & Debug Output Pane */}
              <ConsoleOutput
                output={output}
                onClearOutput={() => setOutput(null)}
                onTriggerDebug={handleTriggerDebug}
                debugResult={debugResult}
                isDebugging={isDebugging}
                onApplyFix={handleApplyFix}
                quickActionResult={quickActionResult}
                isQuickActionLoading={isQuickActionLoading}
                onApplyRefactor={handleApplyRefactor}
                onSaveAsTestFile={handleSaveAsTestFile}
                onExecuteTerminal={api.executeTerminal}
                activeTab={activeConsoleTab}
                setActiveTab={setActiveConsoleTab}
              />
            </>
          ) : (
            <WebPreview activeFile={activeFile} />
          )}
        </div>
      </div>

      {/* Settings Modal */}
      <SettingsModal
        isOpen={settingsOpen}
        onClose={() => setSettingsOpen(false)}
      />
    </div>
  );
}
