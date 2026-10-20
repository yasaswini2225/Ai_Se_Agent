import React, { useState, useEffect } from 'react';
import { Settings, Key, Cpu, Check, X, Shield, ExternalLink, Sparkles } from 'lucide-react';
import { api } from '../services/api';

export default function SettingsModal({ isOpen, onClose }) {
  const [provider, setProvider] = useState('mock');
  const [geminiKey, setGeminiKey] = useState('');
  const [openaiKey, setOpenaiKey] = useState('');
  const [groqKey, setGroqKey] = useState('');
  const [ollamaUrl, setOllamaUrl] = useState('http://localhost:11434');
  const [modelName, setModelName] = useState('gemini-2.5-flash');
  const [savedSuccess, setSavedSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isOpen) {
      loadSettings();
    }
  }, [isOpen]);

  const loadSettings = async () => {
    try {
      const data = await api.getSettings();
      setProvider(data.provider || 'mock');
      setModelName(data.model_name || 'gemini-2.5-flash');
      setOllamaUrl(data.ollama_base_url || 'http://localhost:11434');
    } catch (err) {
      console.error(err);
    }
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await api.updateSettings({
        provider,
        gemini_api_key: geminiKey || undefined,
        openai_api_key: openaiKey || undefined,
        groq_api_key: groqKey || undefined,
        ollama_base_url: ollamaUrl,
        model_name: modelName
      });
      setSavedSuccess(true);
      setTimeout(() => setSavedSuccess(false), 2500);
    } catch (err) {
      alert(`Failed to save settings: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700/80 rounded-2xl w-full max-w-md shadow-2xl overflow-hidden select-none">
        {/* Header */}
        <div className="h-12 px-4 border-b border-slate-800 flex items-center justify-between bg-slate-950">
          <div className="flex items-center space-x-2 text-indigo-400 font-semibold text-sm">
            <Settings className="w-4 h-4" />
            <span>AI Model & Provider Settings</span>
          </div>
          <button onClick={onClose} className="p-1 text-slate-400 hover:text-white rounded">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Form Body */}
        <form onSubmit={handleSave} className="p-4 space-y-4 text-xs">
          {/* Provider Selection */}
          <div>
            <label className="block text-slate-300 font-medium mb-1.5">Active AI Engine / Provider</label>
            <select
              value={provider}
              onChange={(e) => {
                const p = e.target.value;
                setProvider(p);
                if (p === 'gemini') setModelName('gemini-2.5-flash');
                else if (p === 'openai') setModelName('gpt-4o-mini');
                else if (p === 'groq') setModelName('llama-3.3-70b-versatile');
                else if (p === 'ollama') setModelName('llama3');
                else setModelName('devpulse-local-v1');
              }}
              className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-white focus:outline-none focus:border-indigo-500"
            >
              <option value="mock">DevPulse Built-in Offline Engine (Free / No Key Required)</option>
              <option value="gemini">Google Gemini (Recommended - Fast & Powerful)</option>
              <option value="openai">OpenAI (GPT-4o, GPT-4o-mini)</option>
              <option value="groq">Groq (Ultra Fast Llama 3.3)</option>
              <option value="ollama">Local Ollama (Local Self-Hosted)</option>
            </select>
          </div>

          {/* Gemini Key Input */}
          {provider === 'gemini' && (
            <div className="space-y-1.5">
              <label className="block text-slate-300 font-medium flex items-center justify-between">
                <span>Google Gemini API Key</span>
                <a
                  href="https://aistudio.google.com/app/apikey"
                  target="_blank"
                  rel="noreferrer"
                  className="text-indigo-400 hover:underline flex items-center space-x-1 text-[11px]"
                >
                  <span>Get Gemini Key</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              </label>
              <input
                type="password"
                placeholder="AIzaSy..."
                value={geminiKey}
                onChange={(e) => setGeminiKey(e.target.value)}
                className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono focus:outline-none focus:border-indigo-500"
              />
            </div>
          )}

          {/* OpenAI Key Input */}
          {provider === 'openai' && (
            <div className="space-y-1.5">
              <label className="block text-slate-300 font-medium">OpenAI API Key</label>
              <input
                type="password"
                placeholder="sk-..."
                value={openaiKey}
                onChange={(e) => setOpenaiKey(e.target.value)}
                className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono focus:outline-none focus:border-indigo-500"
              />
            </div>
          )}

          {/* Groq Key Input */}
          {provider === 'groq' && (
            <div className="space-y-1.5">
              <label className="block text-slate-300 font-medium">Groq API Key</label>
              <input
                type="password"
                placeholder="gsk_..."
                value={groqKey}
                onChange={(e) => setGroqKey(e.target.value)}
                className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono focus:outline-none focus:border-indigo-500"
              />
            </div>
          )}

          {/* Ollama URL */}
          {provider === 'ollama' && (
            <div className="space-y-1.5">
              <label className="block text-slate-300 font-medium">Ollama Endpoint URL</label>
              <input
                type="text"
                placeholder="http://localhost:11434"
                value={ollamaUrl}
                onChange={(e) => setOllamaUrl(e.target.value)}
                className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono focus:outline-none focus:border-indigo-500"
              />
            </div>
          )}

          {/* Model Name */}
          <div>
            <label className="block text-slate-300 font-medium mb-1.5">Model Name</label>
            <input
              type="text"
              value={modelName}
              onChange={(e) => setModelName(e.target.value)}
              className="w-full bg-slate-950 border border-slate-700 rounded-lg p-2 text-white font-mono focus:outline-none focus:border-indigo-500"
            />
          </div>

          <div className="p-2.5 bg-slate-950/70 border border-slate-800 rounded-lg text-[11px] text-slate-400 flex items-start space-x-2">
            <Shield className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
            <span>
              API keys are stored in server memory session and never leaked. You can also use the free built-in offline engine anytime!
            </span>
          </div>

          {/* Buttons */}
          <div className="flex items-center justify-end space-x-2 pt-2 border-t border-slate-800">
            {savedSuccess && (
              <span className="text-emerald-400 flex items-center space-x-1 text-xs mr-auto">
                <Check className="w-3.5 h-3.5" />
                <span>Settings saved!</span>
              </span>
            )}
            <button
              type="button"
              onClick={onClose}
              className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-4 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white font-medium rounded-lg text-xs shadow transition"
            >
              Save Configuration
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
