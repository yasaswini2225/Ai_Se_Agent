import React, { useRef, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { 
  Save, Sparkles, Check, X, FileCode, Play, Bug, FileCheck, BookOpen, 
  Code2, Braces, RefreshCw
} from 'lucide-react';

export default function EditorArea({
  openTabs,
  activeFile,
  fileContents,
  dirtyFiles,
  onSelectTab,
  onCloseTab,
  onContentChange,
  onSaveFile,
  onRunCode,
  onTriggerDebug,
  onQuickAction,
  isExecuting,
  isQuickActionLoading
}) {
  const editorRef = useRef(null);

  const getLanguage = (path) => {
    if (!path) return 'plaintext';
    const ext = path.split('.').pop().toLowerCase();
    switch (ext) {
      case 'py': return 'python';
      case 'js':
      case 'jsx': return 'javascript';
      case 'ts':
      case 'tsx': return 'typescript';
      case 'html': return 'html';
      case 'css': return 'css';
      case 'json': return 'json';
      case 'md': return 'markdown';
      case 'sh': return 'shell';
      default: return 'plaintext';
    }
  };

  const handleEditorDidMount = (editor, monaco) => {
    editorRef.current = editor;

    // Register Ctrl+S / Cmd+S save shortcut
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => {
      if (activeFile) onSaveFile(activeFile);
    });

    // Register Ctrl+Enter to run
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
      if (activeFile) onRunCode();
    });
  };

  const currentContent = activeFile ? (fileContents[activeFile] ?? '') : '';
  const isDirty = activeFile ? !!dirtyFiles[activeFile] : false;
  const currentLang = getLanguage(activeFile);

  return (
    <div className="flex-1 flex flex-col h-full bg-[#1e1e1e] overflow-hidden select-none">
      {/* Tab Bar & Action Toolbar */}
      <div className="h-10 bg-slate-950 border-b border-slate-800 flex items-center justify-between px-2 overflow-x-auto">
        {/* Open File Tabs */}
        <div className="flex items-center space-x-1 overflow-x-auto max-w-[65%]">
          {openTabs.map((path) => {
            const isActive = activeFile === path;
            const fileName = path.split('/').pop();
            const dirty = !!dirtyFiles[path];

            return (
              <div
                key={path}
                onClick={() => onSelectTab(path)}
                className={`group flex items-center space-x-2 px-3 py-1.5 rounded-t-md text-xs cursor-pointer border-t-2 transition ${
                  isActive
                    ? 'bg-[#1e1e1e] text-white border-indigo-500 font-medium'
                    : 'bg-slate-900/60 text-slate-400 hover:text-slate-200 border-transparent hover:bg-slate-900'
                }`}
              >
                <FileCode className={`w-3.5 h-3.5 ${isActive ? 'text-indigo-400' : 'text-slate-500'}`} />
                <span className="truncate max-w-[130px]">{fileName}</span>
                {dirty ? (
                  <span className="w-2 h-2 rounded-full bg-amber-400 group-hover:hidden" />
                ) : null}
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    onCloseTab(path);
                  }}
                  className={`p-0.5 rounded hover:bg-slate-700 text-slate-400 hover:text-white ${
                    dirty ? 'hidden group-hover:block' : ''
                  }`}
                >
                  <X className="w-3 h-3" />
                </button>
              </div>
            );
          })}
        </div>

        {/* Action Buttons: Save, Run, Quick AI */}
        {activeFile && (
          <div className="flex items-center space-x-1.5">
            {/* Quick AI Action Buttons */}
            <div className="flex items-center space-x-1 mr-1">
              <button
                disabled={isQuickActionLoading}
                onClick={() => onQuickAction('explain')}
                title="Explain selected code with AI"
                className="px-2 py-1 bg-slate-900 hover:bg-slate-800 disabled:opacity-60 text-slate-300 hover:text-white rounded text-[11px] border border-slate-800 flex items-center space-x-1 transition"
              >
                <BookOpen className="w-3 h-3 text-sky-400" />
                <span>Explain</span>
              </button>
              <button
                disabled={isQuickActionLoading}
                onClick={() => onQuickAction('refactor')}
                title="Refactor & optimize code"
                className="px-2 py-1 bg-slate-900 hover:bg-slate-800 disabled:opacity-60 text-slate-300 hover:text-white rounded text-[11px] border border-slate-800 flex items-center space-x-1 transition"
              >
                <Sparkles className="w-3 h-3 text-amber-400" />
                <span>Refactor</span>
              </button>
              <button
                disabled={isQuickActionLoading}
                onClick={() => onQuickAction('test')}
                title="Generate Unit Tests"
                className="px-2 py-1 bg-slate-900 hover:bg-slate-800 disabled:opacity-60 text-slate-300 hover:text-white rounded text-[11px] border border-slate-800 flex items-center space-x-1 transition"
              >
                <FileCheck className="w-3 h-3 text-emerald-400" />
                <span>Tests</span>
              </button>
            </div>

            {/* Save Button */}
            <button
              onClick={() => onSaveFile(activeFile)}
              className={`flex items-center space-x-1 px-2.5 py-1 rounded text-xs font-medium transition ${
                isDirty 
                  ? 'bg-amber-600/30 text-amber-300 border border-amber-500/50 hover:bg-amber-600/40' 
                  : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
              }`}
              title="Save File (Ctrl + S)"
            >
              <Save className="w-3 h-3" />
              <span>{isDirty ? 'Save *' : 'Saved'}</span>
            </button>

            {/* Run Button */}
            <button
              onClick={onRunCode}
              disabled={isExecuting}
              className="flex items-center space-x-1.5 px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-white rounded text-xs font-semibold shadow transition"
              title="Run Script (Ctrl + Enter)"
            >
              {isExecuting ? (
                <div className="w-3 h-3 border-2 border-white border-t-transparent rounded-full animate-spin" />
              ) : (
                <Play className="w-3 h-3 fill-white" />
              )}
              <span>Run</span>
            </button>
          </div>
        )}
      </div>

      {/* Editor Body */}
      {activeFile ? (
        <div className="flex-1 relative">
          <Editor
            height="100%"
            language={currentLang}
            value={currentContent}
            theme="vs-dark"
            onMount={handleEditorDidMount}
            onChange={(val) => onContentChange(activeFile, val || '')}
            options={{
              fontSize: 13,
              fontFamily: "'JetBrains Mono', 'Fira Code', Consolas, monospace",
              fontLigatures: true,
              tabSize: 4,
              minimap: { enabled: true, scale: 0.75 },
              scrollBeyondLastLine: false,
              automaticLayout: true,
              wordWrap: 'on',
              lineNumbers: 'on',
              folding: true,
              cursorBlinking: 'smooth',
              cursorSmoothCaretAnimation: 'on',
              smoothScrolling: true,
              padding: { top: 12, bottom: 12 }
            }}
          />
        </div>
      ) : (
        <div className="flex-1 flex flex-col items-center justify-center text-slate-500 space-y-3">
          <div className="p-4 bg-slate-900/60 rounded-2xl border border-slate-800">
            <Code2 className="w-10 h-10 text-indigo-400/60" />
          </div>
          <div className="text-center">
            <h3 className="text-sm font-medium text-slate-300">No File Opened</h3>
            <p className="text-xs text-slate-500 mt-1">Select a file from the Explorer or run an AI Agent task to begin.</p>
          </div>
        </div>
      )}

      {/* Status Bar */}
      <div className="h-6 bg-slate-950 border-t border-slate-800/80 px-3 flex items-center justify-between text-[11px] text-slate-400 select-none">
        <div className="flex items-center space-x-3">
          <span className="font-mono text-indigo-400">{activeFile || 'No file selected'}</span>
          {activeFile && (
            <span>
              {currentContent.split('\n').length} lines • {currentContent.length} chars
            </span>
          )}
        </div>
        <div className="flex items-center space-x-3">
          <span className="uppercase text-slate-500 font-mono">{currentLang}</span>
          <span className="text-slate-600">UTF-8</span>
          <span className="flex items-center space-x-1 text-emerald-400">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
            <span>Ready</span>
          </span>
        </div>
      </div>
    </div>
  );
}
