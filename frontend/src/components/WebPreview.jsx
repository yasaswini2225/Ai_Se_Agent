import React, { useState } from 'react';
import { ExternalLink, RefreshCw, Globe, ArrowLeft, ArrowRight, Laptop } from 'lucide-react';

export default function WebPreview({ activeFile }) {
  // Determine URL to preview: if active file ends in .html use it, else default to web_game/index.html
  const isHtml = activeFile && activeFile.endsWith('.html');
  const targetPath = isHtml ? activeFile : 'web_game/index.html';
  const previewUrl = `/workspace-preview/${targetPath}`;

  const [refreshKey, setRefreshKey] = useState(0);

  const handleRefresh = () => {
    setRefreshKey(prev => prev + 1);
  };

  return (
    <div className="flex-1 flex flex-col h-full bg-slate-950 select-none">
      {/* Top Browser Bar */}
      <div className="h-10 px-3 bg-slate-900 border-b border-slate-800 flex items-center justify-between text-xs">
        <div className="flex items-center space-x-2">
          <div className="flex space-x-1.5 mr-2">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-500/80 inline-block" />
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500/80 inline-block" />
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500/80 inline-block" />
          </div>
          <button 
            onClick={handleRefresh}
            title="Reload Preview"
            className="p-1 text-slate-400 hover:text-white hover:bg-slate-800 rounded transition"
          >
            <RefreshCw className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Address pill */}
        <div className="flex items-center space-x-1.5 bg-slate-950 border border-slate-800 px-3 py-1 rounded-full text-[11px] text-slate-300 font-mono w-1/2 justify-center">
          <Globe className="w-3 h-3 text-indigo-400" />
          <span className="truncate">localhost:8000/preview/{targetPath}</span>
        </div>

        {/* Open externally */}
        <div>
          <a
            href={previewUrl}
            target="_blank"
            rel="noreferrer"
            className="flex items-center space-x-1 p-1 text-slate-400 hover:text-white hover:bg-slate-800 rounded transition text-xs"
            title="Open in New Tab"
          >
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>
      </div>

      {/* Live Preview Iframe */}
      <div className="flex-1 bg-black relative">
        <iframe
          key={refreshKey}
          src={previewUrl}
          title="DevPulse Web Preview"
          className="w-full h-full border-none"
          sandbox="allow-scripts allow-same-origin allow-forms allow-modals"
        />
      </div>
    </div>
  );
}
