import React, { useState } from 'react';
import { 
  Folder, FolderOpen, FileCode, FileText, ChevronRight, ChevronDown, 
  Plus, FolderPlus, Trash2, Edit2, RefreshCw, Layers, Sparkles, Terminal
} from 'lucide-react';

export default function Sidebar({ 
  tree, 
  activeFile, 
  onSelectFile, 
  onRefreshTree, 
  onCreateFile, 
  onCreateFolder, 
  onDeleteItem, 
  onRenameItem,
  onResetSamples
}) {
  const [expandedFolders, setExpandedFolders] = useState({});
  const [newPrompt, setNewPrompt] = useState(null); // { type: 'file' | 'folder' | 'rename', targetPath: '' }
  const [inputValue, setInputValue] = useState('');

  const toggleFolder = (path) => {
    setExpandedFolders(prev => ({ ...prev, [path]: !prev[path] }));
  };

  const handleCreateSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    if (newPrompt.type === 'file') {
      const fullPath = newPrompt.parentPath ? `${newPrompt.parentPath}/${inputValue.trim()}` : inputValue.trim();
      onCreateFile(fullPath);
    } else if (newPrompt.type === 'folder') {
      const fullPath = newPrompt.parentPath ? `${newPrompt.parentPath}/${inputValue.trim()}` : inputValue.trim();
      onCreateFolder(fullPath);
    } else if (newPrompt.type === 'rename') {
      onRenameItem(newPrompt.targetPath, inputValue.trim());
    }

    setNewPrompt(null);
    setInputValue('');
  };

  const getFileIcon = (name) => {
    const ext = name.split('.').pop().toLowerCase();
    if (['py'].includes(ext)) return <FileCode className="w-4 h-4 text-emerald-400" />;
    if (['js', 'jsx', 'ts', 'tsx'].includes(ext)) return <FileCode className="w-4 h-4 text-amber-400" />;
    if (['html'].includes(ext)) return <FileCode className="w-4 h-4 text-orange-400" />;
    if (['css'].includes(ext)) return <FileCode className="w-4 h-4 text-sky-400" />;
    if (['json'].includes(ext)) return <FileCode className="w-4 h-4 text-yellow-300" />;
    return <FileText className="w-4 h-4 text-slate-400" />;
  };

  const renderTree = (items, parentPath = '') => {
    return items.map((item) => {
      const isFolder = item.type === 'directory';
      const isExpanded = !!expandedFolders[item.path];
      const isSelected = activeFile === item.path;

      if (isFolder) {
        return (
          <div key={item.path} className="select-none">
            <div 
              className="flex items-center justify-between px-2 py-1.5 hover:bg-slate-800/60 rounded-md cursor-pointer group text-xs text-slate-300"
              onClick={() => toggleFolder(item.path)}
            >
              <div className="flex items-center space-x-1.5 overflow-hidden">
                {isExpanded ? <ChevronDown className="w-3.5 h-3.5 text-slate-400" /> : <ChevronRight className="w-3.5 h-3.5 text-slate-400" />}
                {isExpanded ? <FolderOpen className="w-4 h-4 text-indigo-400" /> : <Folder className="w-4 h-4 text-indigo-400" />}
                <span className="truncate font-medium">{item.name}</span>
              </div>
              <div className="opacity-0 group-hover:opacity-100 flex items-center space-x-1">
                <button 
                  title="New File Inside"
                  className="p-1 hover:text-white hover:bg-slate-700/50 rounded"
                  onClick={(e) => {
                    e.stopPropagation();
                    setNewPrompt({ type: 'file', parentPath: item.path });
                    setInputValue('');
                  }}
                >
                  <Plus className="w-3 h-3" />
                </button>
                <button 
                  title="Delete Folder"
                  className="p-1 hover:text-rose-400 hover:bg-slate-700/50 rounded"
                  onClick={(e) => {
                    e.stopPropagation();
                    if (confirm(`Delete folder '${item.name}' and all contents?`)) onDeleteItem(item.path);
                  }}
                >
                  <Trash2 className="w-3 h-3" />
                </button>
              </div>
            </div>
            {isExpanded && item.children && (
              <div className="pl-4 border-l border-slate-800/80 ml-2.5 my-0.5">
                {renderTree(item.children, item.path)}
              </div>
            )}
          </div>
        );
      }

      return (
        <div 
          key={item.path}
          className={`flex items-center justify-between px-2.5 py-1.5 rounded-md cursor-pointer group text-xs transition-colors ${
            isSelected 
              ? 'bg-indigo-600/20 text-indigo-300 font-medium border-l-2 border-indigo-500' 
              : 'text-slate-300 hover:bg-slate-800/50 hover:text-slate-100'
          }`}
          onClick={() => onSelectFile(item.path)}
        >
          <div className="flex items-center space-x-2 truncate">
            {getFileIcon(item.name)}
            <span className="truncate">{item.name}</span>
          </div>
          <div className="opacity-0 group-hover:opacity-100 flex items-center space-x-1">
            <button 
              title="Rename"
              className="p-1 hover:text-sky-300 hover:bg-slate-700/50 rounded"
              onClick={(e) => {
                e.stopPropagation();
                setNewPrompt({ type: 'rename', targetPath: item.path });
                setInputValue(item.path);
              }}
            >
              <Edit2 className="w-3 h-3" />
            </button>
            <button 
              title="Delete File"
              className="p-1 hover:text-rose-400 hover:bg-slate-700/50 rounded"
              onClick={(e) => {
                e.stopPropagation();
                if (confirm(`Delete file '${item.name}'?`)) onDeleteItem(item.path);
              }}
            >
              <Trash2 className="w-3 h-3" />
            </button>
          </div>
        </div>
      );
    });
  };

  return (
    <div className="w-64 bg-slate-950/80 border-r border-slate-800 flex flex-col h-full select-none">
      {/* Workspace Header */}
      <div className="h-11 px-3 border-b border-slate-800/80 flex items-center justify-between text-xs font-semibold text-slate-300 tracking-wider">
        <div className="flex items-center space-x-1.5 text-indigo-400 uppercase">
          <Layers className="w-4 h-4" />
          <span>Explorer</span>
        </div>
        <div className="flex items-center space-x-1">
          <button 
            title="New File"
            className="p-1 text-slate-400 hover:text-white hover:bg-slate-800 rounded transition"
            onClick={() => { setNewPrompt({ type: 'file', parentPath: '' }); setInputValue(''); }}
          >
            <Plus className="w-3.5 h-3.5" />
          </button>
          <button 
            title="New Folder"
            className="p-1 text-slate-400 hover:text-white hover:bg-slate-800 rounded transition"
            onClick={() => { setNewPrompt({ type: 'folder', parentPath: '' }); setInputValue(''); }}
          >
            <FolderPlus className="w-3.5 h-3.5" />
          </button>
          <button 
            title="Refresh Files"
            className="p-1 text-slate-400 hover:text-white hover:bg-slate-800 rounded transition"
            onClick={onRefreshTree}
          >
            <RefreshCw className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* Input Modal/Prompt for New Item or Rename */}
      {newPrompt && (
        <form onSubmit={handleCreateSubmit} className="p-2 border-b border-indigo-500/30 bg-slate-900/90">
          <div className="text-[11px] text-slate-400 mb-1">
            {newPrompt.type === 'file' && 'Create New File:'}
            {newPrompt.type === 'folder' && 'Create New Folder:'}
            {newPrompt.type === 'rename' && 'Rename Path:'}
          </div>
          <div className="flex space-x-1">
            <input 
              autoFocus
              className="flex-1 bg-slate-950 border border-slate-700 rounded px-2 py-1 text-xs text-white focus:outline-none focus:border-indigo-500"
              placeholder={newPrompt.type === 'file' ? 'app.py or src/index.js' : 'folder_name'}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
            />
            <button type="submit" className="px-2 py-1 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs">
              OK
            </button>
            <button 
              type="button" 
              onClick={() => setNewPrompt(null)} 
              className="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs"
            >
              ✕
            </button>
          </div>
        </form>
      )}

      {/* Tree Content */}
      <div className="flex-1 overflow-y-auto p-2 space-y-0.5">
        {tree.length === 0 ? (
          <div className="text-center py-8 text-xs text-slate-500">
            Workspace is empty.<br />
            <button 
              onClick={onResetSamples}
              className="mt-3 px-3 py-1.5 bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 border border-indigo-500/40 rounded-lg text-xs"
            >
              Load Sample Projects
            </button>
          </div>
        ) : (
          renderTree(tree)
        )}
      </div>

      {/* Quick Starter Demos Footer */}
      <div className="p-2.5 border-t border-slate-800/80 bg-slate-950 text-xs">
        <div className="text-[10px] uppercase font-bold text-slate-500 mb-1.5 tracking-wider">Quick Demos</div>
        <div className="space-y-1">
          <button 
            onClick={() => onSelectFile('analytics.py')}
            className="w-full text-left px-2 py-1 rounded bg-slate-900/60 hover:bg-slate-800 text-slate-300 hover:text-white flex items-center justify-between text-[11px]"
          >
            <span>🐍 Python Analytics</span>
            <span className="text-[9px] text-emerald-400 font-mono">Run</span>
          </button>
          <button 
            onClick={() => onSelectFile('web_game/index.html')}
            className="w-full text-left px-2 py-1 rounded bg-slate-900/60 hover:bg-slate-800 text-slate-300 hover:text-white flex items-center justify-between text-[11px]"
          >
            <span>🕹️ CyberSnake Arcade</span>
            <span className="text-[9px] text-sky-400 font-mono">Preview</span>
          </button>
          <button 
            onClick={() => onSelectFile('buggy_sample.py')}
            className="w-full text-left px-2 py-1 rounded bg-slate-900/60 hover:bg-slate-800 text-slate-300 hover:text-white flex items-center justify-between text-[11px]"
          >
            <span>🐞 Buggy Sample</span>
            <span className="text-[9px] text-rose-400 font-mono">Debug</span>
          </button>
        </div>
      </div>
    </div>
  );
}
