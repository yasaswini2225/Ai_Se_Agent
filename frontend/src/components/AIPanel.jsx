import React, { useState, useRef, useEffect } from 'react';
import { 
  Bot, Send, Sparkles, CheckCircle2, AlertCircle, FileCode, ArrowRight, 
  Lightbulb, Play, RotateCcw, Copy, Check, Compass, Cpu, Wand2, Trash2, Code2
} from 'lucide-react';
import { api } from '../services/api';

// Rich Code Block with Copy & Insert-to-Editor Actions
function CodeBlock({ language, code, onInsertCode }) {
  const [copied, setCopied] = useState(false);
  const [inserted, setInserted] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleInsert = () => {
    if (onInsertCode) {
      onInsertCode(code);
      setInserted(true);
      setTimeout(() => setInserted(false), 2000);
    }
  };

  return (
    <div className="my-2 rounded-xl overflow-hidden border border-slate-700/80 bg-[#090b10] shadow-md">
      <div className="flex items-center justify-between px-3 py-1.5 bg-slate-900/90 border-b border-slate-800 text-[10px] text-slate-400">
        <span className="font-mono uppercase font-bold text-indigo-400">{language || 'CODE'}</span>
        <div className="flex items-center space-x-1">
          <button
            onClick={handleCopy}
            className="flex items-center space-x-1 px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition"
            title="Copy code to clipboard"
          >
            {copied ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
            <span>{copied ? 'Copied' : 'Copy'}</span>
          </button>
          {onInsertCode && (
            <button
              onClick={handleInsert}
              className="flex items-center space-x-1 px-2 py-0.5 rounded bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 hover:text-white border border-indigo-500/40 transition"
              title="Insert into active file in Editor"
            >
              {inserted ? <Check className="w-3 h-3 text-emerald-400" /> : <Code2 className="w-3 h-3" />}
              <span>{inserted ? 'Inserted!' : 'Insert'}</span>
            </button>
          )}
        </div>
      </div>
      <pre className="p-3 font-mono text-[11px] text-emerald-300 overflow-x-auto whitespace-pre selection:bg-indigo-500/30">
        {code}
      </pre>
    </div>
  );
}

// Formats message content with markdown headers, bolding, lists, and code fences
function MessageRenderer({ content, onInsertCode }) {
  if (!content) return null;

  // Split content by code fences: ```lang ... ```
  const parts = [];
  const regex = /```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g;
  let lastIndex = 0;
  let match;

  while ((match = regex.exec(content)) !== null) {
    if (match.index > lastIndex) {
      parts.push({ type: 'text', text: content.slice(lastIndex, match.index) });
    }
    parts.push({ type: 'code', language: match[1] || 'text', code: match[2].trimEnd() });
    lastIndex = regex.lastIndex;
  }

  if (lastIndex < content.length) {
    parts.push({ type: 'text', text: content.slice(lastIndex) });
  }

  return (
    <div className="space-y-1">
      {parts.map((part, idx) => {
        if (part.type === 'code') {
          return (
            <CodeBlock
              key={idx}
              language={part.language}
              code={part.code}
              onInsertCode={onInsertCode}
            />
          );
        }

        // Render formatted text lines
        const lines = part.text.split('\n');
        return (
          <div key={idx} className="space-y-1">
            {lines.map((line, lIdx) => {
              const trimmed = line.trim();
              if (!trimmed) return <div key={lIdx} className="h-1.5" />;

              // Headers: ### Title or ## Title
              if (trimmed.startsWith('###')) {
                return (
                  <h4 key={lIdx} className="font-bold text-indigo-300 text-xs mt-2 mb-1 flex items-center space-x-1">
                    <span>{trimmed.replace(/^###\s*/, '')}</span>
                  </h4>
                );
              }
              if (trimmed.startsWith('##')) {
                return (
                  <h3 key={lIdx} className="font-extrabold text-white text-[13px] mt-2 mb-1">
                    {trimmed.replace(/^##\s*/, '')}
                  </h3>
                );
              }
              if (trimmed.startsWith('#')) {
                return (
                  <h2 key={lIdx} className="font-black text-white text-sm mt-2 mb-1">
                    {trimmed.replace(/^#\s*/, '')}
                  </h2>
                );
              }

              // Bullet points
              if (trimmed.startsWith('- ') || trimmed.startsWith('• ') || trimmed.startsWith('* ')) {
                return (
                  <div key={lIdx} className="flex items-start space-x-1.5 pl-1.5 text-slate-300 text-[11px]">
                    <span className="text-indigo-400 font-bold">•</span>
                    <span>{trimmed.replace(/^[-•*]\s*/, '')}</span>
                  </div>
                );
              }

              return (
                <p key={lIdx} className="text-slate-200 text-xs leading-relaxed">
                  {trimmed}
                </p>
              );
            })}
          </div>
        );
      })}
    </div>
  );
}

export default function AIPanel({ 
  activeFile, 
  onOpenFile, 
  onRefreshWorkspace,
  onNavigateToPreview,
  onInsertCode
}) {
  const [activeTab, setActiveTab] = useState('agent'); // 'chat' | 'agent'
  
  // Chat state
  const [chatMessages, setChatMessages] = useState([
    {
      role: 'assistant',
      content: `### 👋 Welcome to DevPulse AI!
I am your **AI Software Engineer & Interactive Coding Assistant**.

Ask me any technical question (e.g. *"How to center a div?"*, *"Explain Two Sum in Python"*, *"What is an event loop?"*), or switch to **Agent Mode** to have me autonomously plan and build applications directly in your workspace!`
    }
  ]);
  const [chatInput, setChatInput] = useState('');
  const [isChatLoading, setIsChatLoading] = useState(false);
  const chatScrollRef = useRef(null);

  // Agent state
  const [agentTask, setAgentTask] = useState('');
  const [isAgentRunning, setIsAgentRunning] = useState(false);
  const [agentResult, setAgentResult] = useState(null);
  const [agentHistory, setAgentHistory] = useState([]);

  useEffect(() => {
    if (chatScrollRef.current) {
      chatScrollRef.current.scrollTop = chatScrollRef.current.scrollHeight;
    }
  }, [chatMessages, isChatLoading]);

  // Handle Send Chat
  const handleSendChat = async (textToSend) => {
    const text = textToSend || chatInput;
    if (!text.trim() || isChatLoading) return;

    const newMessages = [...chatMessages, { role: 'user', content: text }];
    setChatMessages(newMessages);
    setChatInput('');
    setIsChatLoading(true);

    try {
      const response = await api.sendChat(newMessages);
      setChatMessages(prev => [...prev, { role: 'assistant', content: response.reply }]);
    } catch (err) {
      setChatMessages(prev => [
        ...prev, 
        { role: 'assistant', content: `❌ Error connecting to AI: ${err.message}` }
      ]);
    } finally {
      setIsChatLoading(false);
    }
  };

  const handleClearChat = () => {
    setChatMessages([
      {
        role: 'assistant',
        content: `### 👋 Conversation Cleared
Ready for your next coding question or architecture discussion. Ask me anything!`
      }
    ]);
  };

  // Handle Run Agent Task
  const handleRunAgent = async (taskText) => {
    const task = taskText || agentTask;
    if (!task.trim() || isAgentRunning) return;

    setIsAgentRunning(true);
    setAgentResult(null);

    try {
      const result = await api.runAgentTask(task);
      setAgentResult(result);
      setAgentHistory(prev => [
        { task, timestamp: new Date().toLocaleTimeString(), summary: result.summary, files: result.executed_files || [] },
        ...prev
      ]);
      await onRefreshWorkspace();
      
      // Auto-open first generated file if present
      if (result.executed_files && result.executed_files.length > 0) {
        onOpenFile(result.executed_files[0]);
      }
    } catch (err) {
      setAgentResult({
        error: true,
        summary: `Task Execution failed: ${err.message}`,
        plan: [],
        files: []
      });
    } finally {
      setIsAgentRunning(false);
    }
  };

  const [showCatalog, setShowCatalog] = useState(false);
  const [catalogFilter, setCatalogFilter] = useState('');

  const BENCHMARK_TASKS = [
    { title: "Calculator", prompt: "Build a Calculator", category: "Utility" },
    { title: "Student Management System", prompt: "Build a Student Management System", category: "Management" },
    { title: "To-Do List App", prompt: "Create a To-Do List App", category: "Productivity" },
    { title: "Personal Portfolio Website", prompt: "Build a Personal Portfolio Website", category: "Web App" },
    { title: "Login and Registration Page", prompt: "Create a Login and Registration Page", category: "Web App" },
    { title: "Weather App", prompt: "Build a Weather App", category: "Utility" },
    { title: "Notes Application", prompt: "Create a Notes Application", category: "Productivity" },
    { title: "Quiz Application", prompt: "Build a Quiz Application", category: "Education" },
    { title: "Expense Tracker", prompt: "Create an Expense Tracker", category: "Finance" },
    { title: "Simple Chatbot", prompt: "Build a Simple Chatbot", category: "AI & Chat" },
    { title: "Library Management System", prompt: "Create a Library Management System", category: "Management" },
    { title: "E-commerce Website", prompt: "Build an E-commerce Website", category: "Web App" },
    { title: "Password Generator", prompt: "Create a Password Generator", category: "Security" },
    { title: "Digital Clock", prompt: "Build a Digital Clock", category: "Utility" },
    { title: "Number Guessing Game", prompt: "Create a Number Guessing Game", category: "Game" },
    { title: "Tic-Tac-Toe Game", prompt: "Build a Tic-Tac-Toe Game", category: "Game" },
    { title: "Unit Converter", prompt: "Create a Unit Converter", category: "Utility" },
    { title: "BMI Calculator", prompt: "Build a BMI Calculator", category: "Health" },
    { title: "Contact Management System", prompt: "Create a Contact Management System", category: "Management" },
    { title: "Simple Blog Website", prompt: "Build a Simple Blog Website", category: "Web App" },
    { title: "File Organizer Script in Python", prompt: "Create a File Organizer Script in Python", category: "Python Script" },
    { title: "Student Marks Calculator in Java", prompt: "Build a Student Marks Calculator in Java", category: "Java" },
    { title: "Employee Management System", prompt: "Create an Employee Management System", category: "Management" },
    { title: "Currency Converter", prompt: "Build a Currency Converter", category: "Finance" },
    { title: "Form Validation System", prompt: "Create a Form Validation System", category: "Security" },
    { title: "Chat Application", prompt: "Build a Chat Application", category: "AI & Chat" },
    { title: "Resume Builder", prompt: "Create a Resume Builder", category: "Web App" },
    { title: "Snake Game", prompt: "Build a Snake Game", category: "Game" }
  ];

  const agentSuggestions = [
    { title: "Timer & Stopwatch", prompt: "create a timer app" },
    { title: "Student Management", prompt: "Build a Student Management System" },
    { title: "E-Commerce Website", prompt: "Build an E-commerce Website" },
    { title: "Tic-Tac-Toe Game", prompt: "Build a Tic-Tac-Toe Game" },
    { title: "Resume Builder", prompt: "Create a Resume Builder" },
    { title: "Expense Tracker", prompt: "Create an Expense Tracker" }
  ];

  const quickQuestions = [
    { label: "Center a Div", q: "How to center a div in CSS?" },
    { label: "Two Sum", q: "How to solve Two Sum in Python with O(n) complexity?" },
    { label: "Event Loop", q: "Explain how the event loop works in Node.js and JavaScript" },
    { label: "Decorators", q: "Explain Python decorators with a code example" },
    { label: "let vs const", q: "What is the difference between let, const, and var in JavaScript?" },
    { label: "Reverse String", q: "How to reverse a string in Python and JavaScript?" },
    { label: "Binary Search", q: "How does Binary Search work and what is its time complexity?" },
    { label: "REST vs GraphQL", q: "What is the difference between REST API and GraphQL?" },
    { label: "SQL vs NoSQL", q: "Explain the difference between SQL and NoSQL databases" },
    { label: "React Hooks", q: "Explain useState and useEffect in React with example" }
  ];

  return (
    <div className="w-84 lg:w-96 bg-slate-950 border-r border-slate-800 flex flex-col h-full select-none">
      {/* Header Tabs: Chatbot vs Autonomous Agent */}
      <div className="h-11 px-3 border-b border-slate-800/80 flex items-center justify-between bg-slate-950/90">
        <div className="flex bg-slate-900 p-0.5 rounded-lg border border-slate-800 text-xs">
          <button
            onClick={() => setActiveTab('agent')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded-md transition font-medium ${
              activeTab === 'agent' 
                ? 'bg-indigo-600 text-white shadow-sm' 
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>Agent Mode</span>
          </button>
          <button
            onClick={() => setActiveTab('chat')}
            className={`flex items-center space-x-1.5 px-3 py-1 rounded-md transition font-medium ${
              activeTab === 'chat' 
                ? 'bg-indigo-600 text-white shadow-sm' 
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Bot className="w-3.5 h-3.5" />
            <span>Chat Q&A</span>
          </button>
        </div>

        {activeTab === 'chat' && (
          <button
            onClick={handleClearChat}
            title="Clear Chat Conversation"
            className="p-1 text-slate-500 hover:text-rose-400 hover:bg-slate-900 rounded transition text-xs"
          >
            <Trash2 className="w-3.5 h-3.5" />
          </button>
        )}
      </div>

      {/* Mode 1: Autonomous Agent Mode */}
      {activeTab === 'agent' && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Top description */}
          <div className="p-3 bg-gradient-to-b from-indigo-950/20 to-transparent border-b border-slate-800/60">
            <div className="flex items-center space-x-2 text-indigo-300 font-semibold text-xs mb-1">
              <Cpu className="w-4 h-4 text-indigo-400" />
              <span>Autonomous Task Builder</span>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Give any engineering goal. The Agent breaks it down, writes code across files, and saves everything to your workspace.
            </p>
          </div>

          {/* Task Form */}
          <div className="p-3 border-b border-slate-800/80">
            <div className="relative">
              <textarea
                rows={3}
                placeholder="e.g. Build a Calculator, Create a Timer App, Build a Student Management System..."
                value={agentTask}
                onChange={(e) => setAgentTask(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
                    e.preventDefault();
                    handleRunAgent();
                  }
                }}
                className="w-full bg-slate-900 border border-slate-700/80 rounded-xl p-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 resize-none shadow-inner"
              />
              <div className="flex items-center justify-between mt-2">
                <span className="text-[10px] text-slate-500">Ctrl + Enter to dispatch</span>
                <button
                  disabled={!agentTask.trim() || isAgentRunning}
                  onClick={() => handleRunAgent()}
                  className={`flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold shadow-md transition ${
                    isAgentRunning
                      ? 'bg-slate-800 text-slate-500 cursor-not-allowed'
                      : 'bg-gradient-to-r from-indigo-500 to-indigo-600 hover:from-indigo-600 hover:to-indigo-700 text-white'
                  }`}
                >
                  {isAgentRunning ? (
                    <>
                      <div className="w-3.5 h-3.5 border-2 border-indigo-300 border-t-transparent rounded-full animate-spin" />
                      <span>Building...</span>
                    </>
                  ) : (
                    <>
                      <Wand2 className="w-3.5 h-3.5" />
                      <span>Build Task</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Quick Suggestions & 30 Benchmark Tasks Link */}
            {!agentResult && !isAgentRunning && (
              <div className="mt-3">
                <div className="flex items-center justify-between mb-1.5">
                  <span className="text-[10px] font-semibold uppercase tracking-wider text-slate-500">
                    Quick Suggestions
                  </span>
                  <button
                    type="button"
                    onClick={() => setShowCatalog(true)}
                    className="text-[10px] text-indigo-400 hover:text-indigo-300 font-medium flex items-center space-x-1"
                  >
                    <span>Browse Benchmark Tasks →</span>
                  </button>
                </div>
                <div className="grid grid-cols-2 gap-1.5">
                  {agentSuggestions.map((s, idx) => (
                    <button
                      key={idx}
                      onClick={() => {
                        setAgentTask(s.prompt);
                        handleRunAgent(s.prompt);
                      }}
                      className="p-1.5 bg-slate-900/80 hover:bg-slate-800/80 border border-slate-800 hover:border-indigo-500/50 rounded-lg text-left transition group"
                    >
                      <div className="text-[11px] font-medium text-slate-300 group-hover:text-indigo-300 truncate">
                        {s.title}
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Agent Results / Execution Feed */}
          <div className="flex-1 overflow-y-auto p-3 space-y-3">
            {isAgentRunning && (
              <div className="bg-slate-900/90 border border-indigo-500/40 rounded-xl p-4 text-center space-y-3 animate-pulse">
                <div className="inline-block p-3 bg-indigo-500/20 rounded-full text-indigo-400">
                  <Cpu className="w-6 h-6 animate-spin" />
                </div>
                <div>
                  <h4 className="text-xs font-semibold text-white">Agent is Processing Task</h4>
                  <p className="text-[11px] text-slate-400 mt-1">
                    Analyzing constraints, formulating plan, and generating workspace files...
                  </p>
                </div>
              </div>
            )}

            {agentResult && (
              <div className="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5 space-y-3">
                {agentResult.error ? (
                  <div className="text-rose-400 text-xs flex items-center space-x-2">
                    <AlertCircle className="w-4 h-4 shrink-0" />
                    <span>{agentResult.summary}</span>
                  </div>
                ) : (
                  <>
                    <div className="flex items-center space-x-2 text-emerald-400 text-xs font-semibold">
                      <CheckCircle2 className="w-4 h-4" />
                      <span>Task Completed Successfully!</span>
                    </div>

                    <p className="text-xs text-slate-300 leading-relaxed bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
                      {agentResult.summary}
                    </p>

                    {/* Step Plan */}
                    {agentResult.plan && agentResult.plan.length > 0 && (
                      <div className="space-y-1.5">
                        <div className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">
                          Execution Milestones
                        </div>
                        <div className="space-y-1">
                          {agentResult.plan.map((step, i) => (
                            <div key={i} className="flex items-start space-x-2 text-[11px] text-slate-300">
                              <span className="w-4 h-4 rounded-full bg-indigo-950 border border-indigo-500/40 text-indigo-400 flex items-center justify-center shrink-0 text-[10px] font-bold">
                                {i + 1}
                              </span>
                              <span>{step}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Created Files */}
                    {agentResult.files && agentResult.files.length > 0 && (
                      <div className="space-y-1.5 pt-1">
                        <div className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">
                          Artifacts Written ({agentResult.files.length})
                        </div>
                        <div className="space-y-1">
                          {agentResult.files.map((f, i) => (
                            <div 
                              key={i} 
                              onClick={() => onOpenFile(f.path)}
                              className="flex items-center justify-between p-2 bg-slate-950 hover:bg-slate-800/80 border border-slate-800 rounded-lg cursor-pointer transition group"
                            >
                              <div className="flex items-center space-x-2 overflow-hidden">
                                <FileCode className="w-3.5 h-3.5 text-indigo-400 shrink-0" />
                                <span className="text-xs font-mono text-slate-200 group-hover:text-indigo-300 truncate">
                                  {f.path}
                                </span>
                              </div>
                              <span className="text-[10px] text-indigo-400 bg-indigo-950/60 px-1.5 py-0.5 rounded border border-indigo-800/50">
                                Open
                              </span>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Next Steps Guidance */}
                    {agentResult.next_steps && (
                      <div className="bg-indigo-950/30 border border-indigo-500/20 p-2.5 rounded-lg text-[11px] text-indigo-200 flex items-start space-x-2">
                        <Lightbulb className="w-3.5 h-3.5 text-indigo-400 shrink-0 mt-0.5" />
                        <div>
                          <span className="font-semibold">Next Step: </span>
                          {agentResult.next_steps}
                        </div>
                      </div>
                    )}
                  </>
                )}
              </div>
            )}

            {/* Past History */}
            {agentHistory.length > 0 && !isAgentRunning && (
              <div className="pt-2">
                <div className="text-[10px] font-semibold uppercase tracking-wider text-slate-500 mb-1.5">
                  Recent Tasks
                </div>
                <div className="space-y-1.5">
                  {agentHistory.map((h, idx) => (
                    <div key={idx} className="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-xs">
                      <div className="flex justify-between items-center text-slate-400 text-[10px] mb-1">
                        <span className="font-medium text-slate-300 truncate max-w-[180px]">{h.task}</span>
                        <span>{h.timestamp}</span>
                      </div>
                      <div className="text-[11px] text-slate-400 truncate">{h.summary}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Mode 2: Chatbot Q&A Mode */}
      {activeTab === 'chat' && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Chat Messages */}
          <div ref={chatScrollRef} className="flex-1 overflow-y-auto p-3 space-y-3">
            {chatMessages.map((msg, i) => (
              <div 
                key={i} 
                className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'}`}
              >
                <div 
                  className={`max-w-[95%] rounded-2xl p-3.5 text-xs leading-relaxed select-text ${
                    msg.role === 'user'
                      ? 'bg-indigo-600 text-white rounded-br-none shadow-md font-medium'
                      : 'bg-slate-900 border border-slate-800/90 text-slate-200 rounded-bl-none shadow-md'
                  }`}
                >
                  {msg.role === 'user' ? (
                    <div className="whitespace-pre-wrap">{msg.content}</div>
                  ) : (
                    <MessageRenderer content={msg.content} onInsertCode={onInsertCode} />
                  )}
                </div>
              </div>
            ))}

            {isChatLoading && (
              <div className="flex items-center space-x-2 text-xs text-slate-400 bg-slate-900/60 p-2.5 rounded-xl w-32 border border-slate-800">
                <div className="w-3.5 h-3.5 border-2 border-indigo-400 border-t-transparent rounded-full animate-spin" />
                <span>Thinking...</span>
              </div>
            )}
          </div>

          {/* Quick Questions Horizon Chips */}
          <div className="px-3 py-2 bg-slate-950 border-t border-slate-900/90">
            <div className="text-[10px] text-slate-500 uppercase font-bold tracking-wider mb-1.5 flex items-center justify-between">
              <span>Popular Questions</span>
              <span className="text-[9px] text-slate-600">Click to ask</span>
            </div>
            <div className="flex gap-1.5 overflow-x-auto pb-1 text-[11px] text-slate-400 scrollbar-none">
              {quickQuestions.map((item, idx) => (
                <button 
                  key={idx}
                  onClick={() => handleSendChat(item.q)}
                  className="px-2.5 py-1 bg-slate-900 hover:bg-slate-800 hover:text-indigo-300 rounded-lg whitespace-nowrap text-slate-300 border border-slate-800 transition"
                >
                  {item.label}
                </button>
              ))}
            </div>
          </div>

          {/* Chat Input */}
          <div className="p-2.5 border-t border-slate-800/80 bg-slate-950">
            <form 
              onSubmit={(e) => { e.preventDefault(); handleSendChat(); }}
              className="flex items-center space-x-1.5"
            >
              <input
                className="flex-1 bg-slate-900 border border-slate-700/80 rounded-xl px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 shadow-inner"
                placeholder="Ask any programming or architecture question..."
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                disabled={isChatLoading}
              />
              <button
                type="submit"
                disabled={!chatInput.trim() || isChatLoading}
                className="p-2 bg-indigo-600 hover:bg-indigo-500 disabled:bg-slate-800 text-white rounded-xl shadow transition"
              >
                <Send className="w-3.5 h-3.5" />
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Benchmark Tasks Catalog Modal */}
      {showCatalog && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-2xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
            <div className="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-950">
              <div className="flex items-center space-x-2">
                <Sparkles className="w-4 h-4 text-indigo-400" />
                <h3 className="text-sm font-bold text-white">Benchmark Tasks Catalog</h3>
              </div>
              <button 
                onClick={() => setShowCatalog(false)}
                className="p-1 text-slate-400 hover:text-white rounded"
              >
                ✕
              </button>
            </div>

            <div className="p-3 border-b border-slate-800 bg-slate-950/50">
              <input
                type="text"
                placeholder="Search benchmark tasks (e.g. calculator, student, game)..."
                value={catalogFilter}
                onChange={(e) => setCatalogFilter(e.target.value)}
                className="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white outline-none focus:border-indigo-500"
              />
            </div>

            <div className="flex-1 overflow-y-auto p-4 grid grid-cols-1 md:grid-cols-2 gap-2.5">
              {BENCHMARK_TASKS.filter(t => 
                t.title.toLowerCase().includes(catalogFilter.toLowerCase()) || 
                t.category.toLowerCase().includes(catalogFilter.toLowerCase())
              ).map((task, idx) => (
                <div
                  key={idx}
                  onClick={() => {
                    setAgentTask(task.prompt);
                    setShowCatalog(false);
                    handleRunAgent(task.prompt);
                  }}
                  className="p-3 bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-indigo-500 rounded-xl cursor-pointer transition group flex flex-col justify-between"
                >
                  <div className="flex items-start justify-between">
                    <span className="text-xs font-semibold text-slate-200 group-hover:text-indigo-300">
                      {task.title}
                    </span>
                    <span className="text-[10px] px-1.5 py-0.5 rounded bg-indigo-950 text-indigo-300 border border-indigo-800/50">
                      {task.category}
                    </span>
                  </div>
                  <div className="text-[11px] text-slate-400 mt-1 font-mono truncate">
                    {task.prompt}
                  </div>
                </div>
              ))}
            </div>

            <div className="p-3 border-t border-slate-800 bg-slate-950 text-right">
              <button
                onClick={() => setShowCatalog(false)}
                className="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
