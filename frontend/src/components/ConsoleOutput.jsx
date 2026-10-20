import React, { useState } from 'react';
import { 
  Terminal, Bug, Sparkles, CheckCircle2, AlertTriangle, XCircle, 
  Clock, Trash2, ArrowRight, Wand2, Copy, Check, Send
} from 'lucide-react';

export default function ConsoleOutput({
  output,
  onClearOutput,
  onTriggerDebug,
  debugResult,
  isDebugging,
  onApplyFix,
  quickActionResult,
  isQuickActionLoading,
  onApplyRefactor,
  onSaveAsTestFile,
  onExecuteTerminal,
  activeTab,
  setActiveTab
}) {
  const [terminalInput, setTerminalInput] = useState('');
  const [terminalHistory, setTerminalHistory] = useState([
    { cmd: 'dir', out: 'Workspace initialized.' }
  ]);
  const [copied, setCopied] = useState(false);

  const handleCopyCode = (text) => {
    if (!text) return;
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleTerminalSubmit = async (e) => {
    e.preventDefault();
    if (!terminalInput.trim()) return;
    const cmd = terminalInput;
    setTerminalInput('');
    
    try {
      const res = await onExecuteTerminal(cmd);
      setTerminalHistory(prev => [
        ...prev,
        { cmd, out: res.stdout || res.stderr || `(Process exited with code ${res.exit_code})` }
      ]);
    } catch (err) {
      setTerminalHistory(prev => [
        ...prev,
        { cmd, out: `Error executing command: ${err.message}` }
      ]);
    }
  };

  const hasError = output && output.status === 'error';

  return (
    <div className="h-64 bg-slate-950 border-t border-slate-800 flex flex-col select-none">
      {/* Console Tab Headers */}
      <div className="h-9 px-3 border-b border-slate-800/80 flex items-center justify-between bg-slate-950">
        <div className="flex items-center space-x-1 text-xs">
          <button
            onClick={() => setActiveTab('output')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded transition ${
              activeTab === 'output'
                ? 'bg-slate-800 text-white font-medium'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Terminal className="w-3.5 h-3.5" />
            <span>Execution Console</span>
            {output && (
              <span className={`w-2 h-2 rounded-full ${hasError ? 'bg-rose-500 animate-pulse' : 'bg-emerald-500'}`} />
            )}
          </button>

          <button
            onClick={() => setActiveTab('debug')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded transition ${
              activeTab === 'debug'
                ? 'bg-slate-800 text-white font-medium'
                : hasError 
                  ? 'text-rose-400 bg-rose-950/40 border border-rose-800/50 hover:text-rose-300 animate-bounce' 
                  : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Bug className="w-3.5 h-3.5" />
            <span>AI Debugger</span>
            {debugResult && <span className="w-2 h-2 rounded-full bg-indigo-400" />}
          </button>

          <button
            onClick={() => setActiveTab('terminal')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded transition ${
              activeTab === 'terminal'
                ? 'bg-slate-800 text-white font-medium'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <span>Interactive Terminal</span>
          </button>

          <button
            onClick={() => setActiveTab('quickAction')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded transition ${
              activeTab === 'quickAction'
                ? 'bg-slate-800 text-white font-medium'
                : 'text-indigo-400 hover:text-indigo-200'
            }`}
          >
            {isQuickActionLoading ? (
              <div className="w-3.5 h-3.5 border-2 border-indigo-400 border-t-transparent rounded-full animate-spin" />
            ) : (
              <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
            )}
            <span>AI Actions</span>
            {quickActionResult && (
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
            )}
          </button>
        </div>

        {/* Right Console Actions */}
        <div className="flex items-center space-x-2">
          {output && (
            <div className="flex items-center space-x-2 text-[11px] text-slate-400 mr-2">
              <span className="flex items-center space-x-1">
                <Clock className="w-3 h-3 text-slate-500" />
                <span>{output.execution_time_ms} ms</span>
              </span>
              <span className={`px-1.5 py-0.5 rounded text-[10px] font-mono ${
                output.exit_code === 0 ? 'bg-emerald-950 text-emerald-300 border border-emerald-800/60' : 'bg-rose-950 text-rose-300 border border-rose-800/60'
              }`}>
                code {output.exit_code}
              </span>
            </div>
          )}

          {hasError && (
            <button
              onClick={onTriggerDebug}
              disabled={isDebugging}
              className="flex items-center space-x-1 px-2.5 py-1 bg-gradient-to-r from-rose-600 to-indigo-600 hover:from-rose-500 hover:to-indigo-500 text-white text-[11px] font-semibold rounded shadow transition"
            >
              {isDebugging ? (
                <div className="w-3 h-3 border-2 border-white border-t-transparent rounded-full animate-spin" />
              ) : (
                <Wand2 className="w-3 h-3" />
              )}
              <span>Debug with AI</span>
            </button>
          )}

          <button
            onClick={onClearOutput}
            title="Clear Console"
            className="p-1 text-slate-400 hover:text-white hover:bg-slate-800 rounded transition"
          >
            <Trash2 className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* Tab 1: Execution Console Content */}
      {activeTab === 'output' && (
        <div className="flex-1 overflow-y-auto p-3 font-mono text-xs select-text bg-[#0b0d13]">
          {!output ? (
            <div className="text-slate-500 text-xs italic select-none">
              Console output ready. Click "Run" or press Ctrl+Enter to execute code.
            </div>
          ) : (
            <div className="space-y-2">
              {output.stdout && (
                <pre className="text-emerald-300 whitespace-pre-wrap">{output.stdout}</pre>
              )}
              {output.stderr && (
                <div className="bg-rose-950/20 border-l-2 border-rose-500 p-2 rounded">
                  <pre className="text-rose-400 whitespace-pre-wrap">{output.stderr}</pre>
                  <div className="mt-2 flex items-center space-x-2">
                    <span className="text-[11px] text-rose-300">Execution failed.</span>
                    <button
                      onClick={onTriggerDebug}
                      className="text-xs text-indigo-300 underline hover:text-white font-sans"
                    >
                      Ask AI Agent to fix this error →
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Tab 2: AI Debugger Breakdown */}
      {activeTab === 'debug' && (
        <div className="flex-1 overflow-y-auto p-3 bg-slate-900/60 text-xs space-y-3">
          {isDebugging ? (
            <div className="flex flex-col items-center justify-center h-full space-y-2 text-indigo-400">
              <div className="w-6 h-6 border-2 border-indigo-400 border-t-transparent rounded-full animate-spin" />
              <p className="text-xs text-slate-300 font-medium">AI Debugger is inspecting traceback and root cause...</p>
            </div>
          ) : debugResult ? (
            <div className="space-y-3 select-text">
              {/* Root Cause Card */}
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <div className="text-[10px] uppercase font-bold text-rose-400 tracking-wider mb-1 flex items-center space-x-1.5">
                  <AlertTriangle className="w-3.5 h-3.5" />
                  <span>Root Cause</span>
                </div>
                <div className="text-slate-200 font-medium">{debugResult.root_cause}</div>
              </div>

              {/* Detailed Diagnosis */}
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <div className="text-[10px] uppercase font-bold text-sky-400 tracking-wider mb-1">
                  Diagnosis & Explanation
                </div>
                <div className="text-slate-300 leading-relaxed whitespace-pre-wrap font-sans">
                  {debugResult.diagnosis}
                </div>
              </div>

              {/* Fix Diff & Apply Button */}
              {debugResult.fixed_code && (
                <div className="bg-slate-950 p-3 rounded-xl border border-indigo-500/30 flex items-center justify-between">
                  <div>
                    <div className="text-[10px] uppercase font-bold text-indigo-400 tracking-wider">
                      Ready Fix Available
                    </div>
                    <div className="text-slate-400 text-[11px] mt-0.5">
                      {debugResult.diff_summary || 'Validated patch generated by AI.'}
                    </div>
                  </div>
                  <button
                    onClick={() => onApplyFix(debugResult.fixed_code)}
                    className="flex items-center space-x-1.5 px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-semibold shadow transition"
                  >
                    <Wand2 className="w-3.5 h-3.5" />
                    <span>Apply Fix to Editor</span>
                  </button>
                </div>
              )}
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center h-full text-slate-500 space-y-2">
              <Bug className="w-8 h-8 text-slate-600" />
              <p>No active debugging session.</p>
              {hasError && (
                <button
                  onClick={onTriggerDebug}
                  className="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-xs"
                >
                  Start AI Debugging
                </button>
              )}
            </div>
          )}
        </div>
      )}

      {/* Tab 3: Interactive Terminal */}
      {activeTab === 'terminal' && (
        <div className="flex-1 flex flex-col bg-[#0b0d13] p-2 text-xs font-mono">
          <div className="flex-1 overflow-y-auto space-y-2 p-1 select-text">
            {terminalHistory.map((item, idx) => (
              <div key={idx} className="space-y-0.5">
                <div className="text-indigo-400 flex items-center space-x-1">
                  <span className="text-slate-600">PS workspace&gt;</span>
                  <span>{item.cmd}</span>
                </div>
                <pre className="text-slate-300 text-[11px] pl-3 whitespace-pre-wrap">{item.out}</pre>
              </div>
            ))}
          </div>
          <form onSubmit={handleTerminalSubmit} className="flex items-center space-x-1 border-t border-slate-800 pt-1.5">
            <span className="text-indigo-400 text-xs font-bold pl-1">&gt;</span>
            <input
              className="flex-1 bg-transparent border-none text-xs text-white focus:outline-none font-mono"
              placeholder="Execute command (e.g. dir, python --version, pip list)..."
              value={terminalInput}
              onChange={(e) => setTerminalInput(e.target.value)}
            />
            <button type="submit" className="p-1 text-slate-400 hover:text-white">
              <Send className="w-3.5 h-3.5" />
            </button>
          </form>
        </div>
      )}

      {/* Tab 4: Quick Action AI Result */}
      {activeTab === 'quickAction' && (
        <div className="flex-1 overflow-y-auto p-4 bg-[#0a0c12] text-xs font-sans text-slate-200 select-text">
          {isQuickActionLoading ? (
            <div className="flex flex-col items-center justify-center h-full text-slate-400 space-y-3 py-8">
              <div className="w-8 h-8 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin" />
              <div className="text-sm font-semibold text-white">Analyzing code with DevPulse AI...</div>
              <p className="text-slate-500 text-xs text-center max-w-sm">
                Parsing syntax, evaluating time/space complexity, and constructing optimized code or test suites.
              </p>
            </div>
          ) : quickActionResult ? (
            (() => {
              const res = typeof quickActionResult === 'string'
                ? { action: 'insight', summary: quickActionResult, markdown: quickActionResult, code: null }
                : quickActionResult;

              const actionLabels = {
                explain: { title: 'Code Architectural Explanation', color: 'text-sky-400 bg-sky-950/40 border-sky-800/60' },
                refactor: { title: 'Code Refactoring & Modernization', color: 'text-indigo-400 bg-indigo-950/40 border-indigo-800/60' },
                test: { title: 'Automated Unit Test Suite', color: 'text-emerald-400 bg-emerald-950/40 border-emerald-800/60' }
              };
              const actionMeta = actionLabels[res.action] || { title: 'AI Engineering Action', color: 'text-indigo-400 bg-indigo-950/40 border-indigo-800/60' };

              return (
                <div className="space-y-4 max-w-4xl mx-auto pb-4">
                  {/* Action Header Card */}
                  <div className="flex items-center justify-between p-3 bg-slate-900/90 rounded-xl border border-slate-800 shadow-sm">
                    <div className="flex items-center space-x-2.5">
                      <span className={`px-2.5 py-1 rounded-md text-[11px] font-bold uppercase tracking-wider border ${actionMeta.color}`}>
                        {res.action || 'AI Action'}
                      </span>
                      <span className="text-slate-100 font-semibold text-xs sm:text-sm">
                        {actionMeta.title}
                      </span>
                    </div>

                    {/* Action Execution Buttons */}
                    <div className="flex items-center space-x-2">
                      {res.code && (
                        <button
                          onClick={() => handleCopyCode(res.code)}
                          className="flex items-center space-x-1 px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded transition"
                          title="Copy Code to Clipboard"
                        >
                          {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                          <span>{copied ? 'Copied!' : 'Copy Code'}</span>
                        </button>
                      )}

                      {res.action === 'refactor' && res.code && onApplyRefactor && (
                        <button
                          onClick={() => onApplyRefactor(res.code)}
                          className="flex items-center space-x-1.5 px-3 py-1.5 bg-gradient-to-r from-indigo-600 to-sky-600 hover:from-indigo-500 hover:to-sky-500 text-white text-xs font-semibold rounded-lg shadow transition"
                        >
                          <Wand2 className="w-3.5 h-3.5" />
                          <span>Apply to Editor</span>
                        </button>
                      )}

                      {(res.action === 'test' || res.action === 'tests') && res.code && onSaveAsTestFile && (
                        <button
                          onClick={() => onSaveAsTestFile(res.code)}
                          className="flex items-center space-x-1.5 px-3 py-1.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-semibold rounded-lg shadow transition"
                        >
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Save as Test File</span>
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Summary Card */}
                  {res.summary && (
                    <div className="p-3 bg-slate-900/60 rounded-xl border border-slate-800/80">
                      <div className="text-[10px] uppercase font-bold text-slate-400 tracking-wider mb-1">
                        Executive Summary
                      </div>
                      <div className="text-slate-300 leading-relaxed font-sans text-xs">
                        {res.summary}
                      </div>
                    </div>
                  )}

                  {/* Markdown or Detailed Breakdown */}
                  {res.markdown && (
                    <div className="p-4 bg-slate-900/40 rounded-xl border border-slate-800/80 text-slate-200 text-xs leading-relaxed whitespace-pre-wrap font-sans">
                      {res.markdown}
                    </div>
                  )}

                  {/* Structured Code Preview if present */}
                  {res.code && (
                    <div className="rounded-xl border border-slate-800 overflow-hidden bg-[#07090e]">
                      <div className="flex items-center justify-between px-3 py-1.5 bg-slate-900/80 border-b border-slate-800 text-[11px] text-slate-400">
                        <span className="font-mono">Generated Output</span>
                        <button
                          onClick={() => handleCopyCode(res.code)}
                          className="text-slate-400 hover:text-white flex items-center space-x-1"
                        >
                          {copied ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                          <span>{copied ? 'Copied' : 'Copy'}</span>
                        </button>
                      </div>
                      <pre className="p-3 text-[11px] font-mono text-emerald-300 overflow-x-auto whitespace-pre">
                        {res.code}
                      </pre>
                    </div>
                  )}
                </div>
              );
            })()
          ) : (
            <div className="flex flex-col items-center justify-center h-full text-slate-500 space-y-2 py-8">
              <Sparkles className="w-8 h-8 text-indigo-400/60" />
              <div className="text-slate-300 font-medium text-xs">Ready for AI Actions</div>
              <p className="text-slate-500 text-[11px] text-center max-w-sm">
                Open any file and click <span className="text-sky-400 font-semibold">Explain</span>, <span className="text-indigo-400 font-semibold">Refactor</span>, or <span className="text-emerald-400 font-semibold">Tests</span> in the editor toolbar above.
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
