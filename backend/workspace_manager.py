import os
import shutil
import zipfile
import io
from pathlib import Path
from typing import List, Dict, Any, Optional
from .config import WORKSPACE_DIR

def get_safe_path(rel_path: str) -> Path:
    # Remove leading slashes and normalize
    clean_path = rel_path.lstrip("/\\")
    target = (WORKSPACE_DIR / clean_path).resolve()
    # Security check: ensure target is inside WORKSPACE_DIR
    if not str(target).startswith(str(WORKSPACE_DIR.resolve())):
        raise ValueError("Access outside workspace directory is forbidden")
    return target

def list_workspace_tree(dir_path: Optional[Path] = None, rel_prefix: str = "") -> List[Dict[str, Any]]:
    if dir_path is None:
        dir_path = WORKSPACE_DIR

    items = []
    try:
        entries = sorted(list(dir_path.iterdir()), key=lambda e: (not e.is_dir(), e.name.lower()))
        for entry in entries:
            # Skip hidden files like .git or __pycache__
            if entry.name.startswith(".") or entry.name == "__pycache__":
                continue
            
            rel = (Path(rel_prefix) / entry.name).as_posix() if rel_prefix else entry.name
            if entry.is_dir():
                items.append({
                    "name": entry.name,
                    "path": rel,
                    "type": "directory",
                    "children": list_workspace_tree(entry, rel)
                })
            else:
                items.append({
                    "name": entry.name,
                    "path": rel,
                    "type": "file",
                    "size": entry.stat().st_size,
                    "extension": entry.suffix.lstrip(".").lower()
                })
    except Exception as e:
        pass
    return items

def read_workspace_file(rel_path: str) -> Dict[str, Any]:
    target = get_safe_path(rel_path)
    if not target.exists() or not target.is_file():
        raise FileNotFoundError(f"File not found: {rel_path}")
    
    try:
        content = target.read_text(encoding="utf-8")
        return {"path": rel_path, "content": content, "size": target.stat().st_size}
    except UnicodeDecodeError:
        return {"path": rel_path, "content": "[Binary file cannot be displayed]", "is_binary": True}

def write_workspace_file(rel_path: str, content: str) -> Dict[str, Any]:
    target = get_safe_path(rel_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return {"path": rel_path, "size": target.stat().st_size, "success": True}

def delete_workspace_item(rel_path: str) -> Dict[str, Any]:
    target = get_safe_path(rel_path)
    if not target.exists():
        raise FileNotFoundError(f"Path not found: {rel_path}")
    
    if target.is_dir():
        shutil.rmtree(target)
    else:
        target.unlink()
    return {"path": rel_path, "success": True}

def rename_workspace_item(old_rel_path: str, new_rel_path: str) -> Dict[str, Any]:
    old_target = get_safe_path(old_rel_path)
    new_target = get_safe_path(new_rel_path)
    if not old_target.exists():
        raise FileNotFoundError(f"Path not found: {old_rel_path}")
    new_target.parent.mkdir(parents=True, exist_ok=True)
    old_target.rename(new_target)
    return {"old_path": old_rel_path, "new_path": new_rel_path, "success": True}

def create_workspace_folder(rel_path: str) -> Dict[str, Any]:
    target = get_safe_path(rel_path)
    target.mkdir(parents=True, exist_ok=True)
    return {"path": rel_path, "success": True}

def export_workspace_zip() -> io.BytesIO:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(WORKSPACE_DIR):
            for file in files:
                file_path = Path(root) / file
                rel_path = file_path.relative_to(WORKSPACE_DIR)
                zf.write(file_path, arcname=str(rel_path))
    buf.seek(0)
    return buf

def seed_sample_projects():
    """Seed sample starter files if the workspace is empty or if core samples are missing"""
    analytics_exists = (WORKSPACE_DIR / "analytics.py").exists()
    web_game_exists = (WORKSPACE_DIR / "web_game" / "index.html").exists()
    buggy_exists = (WORKSPACE_DIR / "buggy_sample.py").exists()

    if analytics_exists and web_game_exists and buggy_exists:
        return

    # 1. Python Data & Algorithm Demo (with intentional bug toggle for testing debugging)
    python_code = '''"""
DevPulse AI - Python Algorithmic Analysis Demo
Demonstrates data processing, statistics, and algorithm simulation.
"""
import time
import math
import random

def calculate_analytics(data):
    total = sum(data)
    n = len(data)
    mean = total / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    return {
        "count": n,
        "sum": total,
        "mean": round(mean, 2),
        "std_dev": round(std_dev, 2),
        "min": min(data),
        "max": max(data)
    }

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    print("🚀 DevPulse AI Engine - Running Python Environment")
    print("-" * 50)
    
    # Generate dataset
    random.seed(42)
    sample_data = [random.randint(10, 100) for _ in range(25)]
    print(f"📊 Raw Dataset ({len(sample_data)} samples):")
    print(sample_data[:10], "... [truncated]")
    
    # Calculate stats
    stats = calculate_analytics(sample_data)
    print("\\n📈 Descriptive Statistics:")
    for k, v in stats.items():
        print(f"   • {k.capitalize()}: {v}")
        
    # Sort
    start_t = time.perf_counter()
    sorted_data = quick_sort(sample_data)
    dur = (time.perf_counter() - start_t) * 1000
    print(f"\\n⚡ QuickSort completed in {dur:.3f} ms:")
    print("   Sorted:", sorted_data[:10], "...")
    print("\\n✅ Execution successful!")
'''
    write_workspace_file("analytics.py", python_code)

    # 2. Modern Interactive Snake / Arcade Web Game
    html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CyberSnake Arcade - DevPulse AI</title>
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
</head>
<body>
  <div class="arcade-container">
    <header class="header">
      <div class="logo">
        <span class="badge">LIVE PREVIEW</span>
        <h1>⚡ CYBER SNAKE</h1>
      </div>
      <div class="header-actions">
        <button id="sound-btn" class="icon-btn" title="Toggle Sound">🔊</button>
        <button id="pause-btn" class="icon-btn" title="Pause / Resume">⏸️</button>
      </div>
      <div class="scoreboard">
        <div class="stat"><span class="label">SCORE</span><span id="score" class="value">0</span></div>
        <div class="stat"><span class="label">HIGH</span><span id="high-score" class="value">0</span></div>
        <div class="stat"><span class="label">SPEED</span><span id="speed" class="value">1.0x</span></div>
      </div>
    </header>

    <div class="canvas-wrapper">
      <canvas id="gameCanvas" width="400" height="400"></canvas>
      <div id="overlay" class="overlay">
        <div class="overlay-card">
          <h2 id="overlay-title">READY TO PLAY?</h2>
          <p id="overlay-msg">Use Arrow Keys or WASD to navigate.</p>
          <button id="start-btn" class="primary-btn">START GAME</button>
        </div>
      </div>
    </div>

    <!-- On-Screen D-Pad for Mouse / Mobile Play -->
    <div class="dpad-box">
      <div></div>
      <button class="dpad-btn" id="dpad-up">▲</button>
      <div></div>
      <button class="dpad-btn" id="dpad-left">◀</button>
      <button class="dpad-btn" id="dpad-pause">⏸</button>
      <button class="dpad-btn" id="dpad-right">▶</button>
      <div></div>
      <button class="dpad-btn" id="dpad-down">▼</button>
      <div></div>
    </div>

    <div class="controls-hint">
      <span>🕹️ Controls: <b>WASD</b> / <b>Arrow Keys</b></span>
      <span>⏸️ Pause: <b>Space</b></span>
    </div>
  </div>
  <script src="game.js"></script>
</body>
</html>
'''
    write_workspace_file("web_game/index.html", html_code)

    css_code = '''* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  user-select: none;
}

body {
  background: radial-gradient(circle at 50% 20%, #1e1b4b 0%, #09090b 100%);
  color: #f1f5f9;
  font-family: 'Plus Jakarta Sans', sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  overflow-x: hidden;
}

.arcade-container {
  background: rgba(18, 18, 24, 0.88);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(99, 102, 241, 0.28);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 40px rgba(99, 102, 241, 0.18);
  display: flex;
  flex-direction: column;
  gap: 14px;
  width: 100%;
  max-width: 440px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 12px;
}

.logo {
  display: flex;
  flex-direction: column;
}

.badge {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 1px;
  color: #818cf8;
  background: rgba(99, 102, 241, 0.15);
  padding: 2px 7px;
  border-radius: 10px;
  display: inline-block;
  margin-bottom: 3px;
  width: fit-content;
}

.header h1 {
  font-size: 18px;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #a5b4fc 0%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.header-actions {
  display: flex;
  gap: 6px;
}

.icon-btn {
  background: #171928;
  border: 1px solid rgba(99, 102, 241, 0.3);
  color: #cbd5e1;
  border-radius: 8px;
  padding: 4px 8px;
  font-size: 13px;
  cursor: pointer;
  transition: 0.15s;
}

.icon-btn:hover {
  background: #252a42;
  color: white;
}

.scoreboard {
  display: flex;
  gap: 10px;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.stat .label {
  font-size: 9px;
  letter-spacing: 1px;
  color: #94a3b8;
  font-weight: 700;
}

.stat .value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 15px;
  font-weight: 800;
  color: #38bdf8;
}

.canvas-wrapper {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid rgba(99, 102, 241, 0.4);
  background: #09090f;
  box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.85);
}

#gameCanvas {
  display: block;
  width: 100%;
  aspect-ratio: 1;
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(9, 9, 15, 0.88);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  transition: opacity 0.25s ease;
}

.overlay.hidden {
  opacity: 0;
  pointer-events: none;
}

.overlay-card {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
}

.overlay-card h2 {
  font-size: 22px;
  font-weight: 800;
  color: #f8fafc;
}

.overlay-card p {
  font-size: 13px;
  color: #94a3b8;
}

.primary-btn {
  background: linear-gradient(135deg, #6366f1 0%, #38bdf8 100%);
  color: white;
  border: none;
  font-size: 13px;
  font-weight: 700;
  padding: 10px 24px;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
  transition: all 0.2s ease;
}

.primary-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(56, 189, 248, 0.5);
}

.dpad-box {
  display: grid;
  grid-template-columns: repeat(3, 40px);
  grid-template-rows: repeat(3, 40px);
  gap: 6px;
  justify-content: center;
  margin-top: 2px;
}

.dpad-btn {
  background: #141726;
  border: 1px solid rgba(99, 102, 241, 0.25);
  color: #cbd5e1;
  border-radius: 8px;
  font-size: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: 0.15s;
}

.dpad-btn:active {
  background: #6366f1;
  color: white;
  transform: scale(0.95);
}

.controls-hint {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: #64748b;
  padding-top: 4px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.controls-hint b {
  color: #cbd5e1;
}
'''
    write_workspace_file("web_game/style.css", css_code)

    js_code = '''// Web Audio Synthesizer
class SoundController {
  constructor() {
    this.ctx = null;
    this.muted = false;
  }
  init() {
    if (!this.ctx) {
      const AC = window.AudioContext || window.webkitAudioContext;
      if (AC) this.ctx = new AC();
    }
  }
  playTone(freq, type = 'sine', duration = 0.08, endFreq = null) {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      if (endFreq) {
        osc.frequency.exponentialRampToValueAtTime(endFreq, this.ctx.currentTime + duration);
      }
      gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    } catch (e) {}
  }
  eat() { this.playTone(480, 'triangle', 0.09, 880); }
  turn() { this.playTone(280, 'sine', 0.02); }
  crash() { this.playTone(320, 'sawtooth', 0.3, 70); }
  pause() { this.playTone(500, 'sine', 0.05); }
}

const sound = new SoundController();
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const highScoreEl = document.getElementById('high-score');
const speedEl = document.getElementById('speed');
const overlay = document.getElementById('overlay');
const overlayTitle = document.getElementById('overlay-title');
const overlayMsg = document.getElementById('overlay-msg');
const startBtn = document.getElementById('start-btn');
const soundBtn = document.getElementById('sound-btn');
const pauseBtn = document.getElementById('pause-btn');

const GRID_SIZE = 20;
const TILE_COUNT = canvas.width / GRID_SIZE;

let snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
let dx = 1;
let dy = 0;
let inputQueue = [];
let food = { x: 15, y: 10 };
let score = 0;
let highScore = parseInt(localStorage.getItem('cybersnake_highscore') || '0', 10);
highScoreEl.textContent = highScore;

let isRunning = false;
let isPaused = false;
let baseSpeed = 115;
let currentSpeed = baseSpeed;
let gameTimer = null;
let particles = [];

function spawnParticles(x, y, color = '#38bdf8', count = 12) {
  const cx = x * GRID_SIZE + GRID_SIZE / 2;
  const cy = y * GRID_SIZE + GRID_SIZE / 2;
  for (let i = 0; i < count; i++) {
    const angle = Math.random() * Math.PI * 2;
    const spd = Math.random() * 3 + 1;
    particles.push({
      x: cx, y: cy,
      vx: Math.cos(angle) * spd,
      vy: Math.sin(angle) * spd,
      color,
      alpha: 1,
      decay: Math.random() * 0.04 + 0.02
    });
  }
}

function spawnFood() {
  while (true) {
    food = {
      x: Math.floor(Math.random() * TILE_COUNT),
      y: Math.floor(Math.random() * TILE_COUNT)
    };
    const onSnake = snake.some(part => part.x === food.x && part.y === food.y);
    if (!onSnake) break;
  }
}

function drawGame() {
  // Clear canvas
  ctx.fillStyle = '#090a12';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Subtle grid
  ctx.strokeStyle = 'rgba(99, 102, 241, 0.05)';
  for (let i = 0; i < canvas.width; i += GRID_SIZE) {
    ctx.beginPath();
    ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height);
    ctx.moveTo(0, i); ctx.lineTo(canvas.width, i);
    ctx.stroke();
  }

  // Draw particles
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.alpha -= p.decay;
    if (p.alpha <= 0) {
      particles.splice(i, 1);
    } else {
      ctx.save();
      ctx.globalAlpha = p.alpha;
      ctx.fillStyle = p.color;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }

  // Draw Food with neon glow
  ctx.save();
  ctx.shadowColor = '#f43f5e';
  ctx.shadowBlur = 12;
  ctx.fillStyle = '#f43f5e';
  ctx.beginPath();
  ctx.arc(food.x * GRID_SIZE + GRID_SIZE / 2, food.y * GRID_SIZE + GRID_SIZE / 2, GRID_SIZE / 2 - 2, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = '#ffffff';
  ctx.beginPath();
  ctx.arc(food.x * GRID_SIZE + GRID_SIZE / 2 - 2, food.y * GRID_SIZE + GRID_SIZE / 2 - 2, 2, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();

  // Draw Snake
  snake.forEach((part, index) => {
    const isHead = index === 0;
    ctx.save();
    if (isHead) {
      ctx.fillStyle = '#38bdf8';
      ctx.shadowColor = '#38bdf8';
      ctx.shadowBlur = 10;
    } else {
      ctx.fillStyle = '#6366f1';
      ctx.shadowBlur = 0;
    }
    const px = part.x * GRID_SIZE + 1.5;
    const py = part.y * GRID_SIZE + 1.5;
    const size = GRID_SIZE - 3;
    ctx.beginPath();
    ctx.roundRect(px, py, size, size, isHead ? 6 : 4);
    ctx.fill();

    // Eyes on head
    if (isHead) {
      ctx.fillStyle = '#ffffff';
      const off = 4;
      let e1 = { x: px + off, y: py + off };
      let e2 = { x: px + size - off, y: py + off };
      if (dy === 1) {
        e1 = { x: px + off, y: py + size - off };
        e2 = { x: px + size - off, y: py + size - off };
      } else if (dx === 1) {
        e1 = { x: px + size - off, y: py + off };
        e2 = { x: px + size - off, y: py + size - off };
      } else if (dx === -1) {
        e1 = { x: px + off, y: py + off };
        e2 = { x: px + off, y: py + size - off };
      }
      ctx.beginPath();
      ctx.arc(e1.x, e1.y, 2, 0, Math.PI * 2);
      ctx.arc(e2.x, e2.y, 2, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  });
}

function updateGame() {
  if (!isRunning || isPaused) return;

  // Process input queue to avoid self-reversal bug
  if (inputQueue.length > 0) {
    const next = inputQueue.shift();
    if ((next.dx !== -dx || dx === 0) && (next.dy !== -dy || dy === 0)) {
      dx = next.dx;
      dy = next.dy;
      sound.turn();
    }
  }

  const head = { x: snake[0].x + dx, y: snake[0].y + dy };

  // Wall collision
  if (head.x < 0 || head.x >= TILE_COUNT || head.y < 0 || head.y >= TILE_COUNT) {
    return gameOver();
  }

  // Self collision
  for (let part of snake) {
    if (head.x === part.x && head.y === part.y) {
      return gameOver();
    }
  }

  snake.unshift(head);

  if (head.x === food.x && head.y === food.y) {
    score += 10;
    sound.eat();
    spawnParticles(food.x, food.y, '#38bdf8', 16);
    scoreEl.textContent = score;
    if (score > highScore) {
      highScore = score;
      highScoreEl.textContent = highScore;
      localStorage.setItem('cybersnake_highscore', highScore);
    }
    // Dynamic Speed Scaling
    const speedMultiplier = 1 + Math.floor(score / 40) * 0.15;
    speedEl.textContent = speedMultiplier.toFixed(1) + 'x';
    currentSpeed = Math.max(45, Math.round(baseSpeed / speedMultiplier));

    spawnFood();
  } else {
    snake.pop();
  }

  drawGame();
  gameTimer = setTimeout(updateGame, currentSpeed);
}

function startGame() {
  snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
  dx = 1;
  dy = 0;
  inputQueue = [];
  score = 0;
  currentSpeed = baseSpeed;
  scoreEl.textContent = score;
  speedEl.textContent = '1.0x';
  spawnFood();
  overlay.classList.add('hidden');
  isRunning = true;
  isPaused = false;
  pauseBtn.textContent = '⏸️';
  clearTimeout(gameTimer);
  updateGame();
}

function togglePause() {
  if (!isRunning) return;
  isPaused = !isPaused;
  sound.pause();
  if (isPaused) {
    clearTimeout(gameTimer);
    pauseBtn.textContent = '▶️';
    overlayTitle.textContent = 'GAME PAUSED';
    overlayMsg.textContent = 'Press Space or Resume to continue.';
    startBtn.textContent = 'RESUME';
    overlay.classList.remove('hidden');
  } else {
    pauseBtn.textContent = '⏸️';
    overlay.classList.add('hidden');
    updateGame();
  }
}

function gameOver() {
  isRunning = false;
  clearTimeout(gameTimer);
  sound.crash();
  spawnParticles(snake[0].x, snake[0].y, '#f43f5e', 24);
  drawGame();
  overlayTitle.textContent = 'GAME OVER';
  overlayMsg.textContent = `Score: ${score} points | High: ${highScore} pts`;
  startBtn.textContent = 'PLAY AGAIN';
  overlay.classList.remove('hidden');
}

function queueDirection(newDx, newDy) {
  if (!isRunning) {
    startGame();
    return;
  }
  if (isPaused) {
    togglePause();
  }
  inputQueue.push({ dx: newDx, dy: newDy });
}

window.addEventListener('keydown', (e) => {
  const gameKeys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Space'];
  if (gameKeys.includes(e.code) || ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) {
    e.preventDefault();
  }

  if (e.code === 'Space' || e.key === ' ') {
    if (!isRunning) startGame();
    else togglePause();
    return;
  }

  switch (e.key) {
    case 'ArrowUp':
    case 'w':
    case 'W':
      queueDirection(0, -1);
      break;
    case 'ArrowDown':
    case 's':
    case 'S':
      queueDirection(0, 1);
      break;
    case 'ArrowLeft':
    case 'a':
    case 'A':
      queueDirection(-1, 0);
      break;
    case 'ArrowRight':
    case 'd':
    case 'D':
      queueDirection(1, 0);
      break;
  }
});

// D-Pad and Header Actions
document.getElementById('dpad-up').addEventListener('click', () => queueDirection(0, -1));
document.getElementById('dpad-down').addEventListener('click', () => queueDirection(0, 1));
document.getElementById('dpad-left').addEventListener('click', () => queueDirection(-1, 0));
document.getElementById('dpad-right').addEventListener('click', () => queueDirection(1, 0));
document.getElementById('dpad-pause').addEventListener('click', togglePause);

startBtn.addEventListener('click', () => {
  if (isPaused) togglePause();
  else startGame();
});
pauseBtn.addEventListener('click', togglePause);
soundBtn.addEventListener('click', () => {
  sound.muted = !sound.muted;
  soundBtn.textContent = sound.muted ? '🔇' : '🔊';
});

drawGame();
'''
    write_workspace_file("web_game/game.js", js_code)

    # 3. JavaScript / Node.js algorithm sample
    node_code = '''// DevPulse AI - Node.js Async Simulation
const simulateTask = (name, delay) => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(`[${new Date().toISOString().slice(11, 19)}] Task '${name}' completed in ${delay}ms`);
    }, delay);
  });
};

async function runPipeline() {
  console.log("⚡ Initiating Async Microservices Pipeline...");
  const tasks = [
    simulateTask("Auth-Service", 200),
    simulateTask("Database-Fetch", 450),
    simulateTask("Cache-Warmup", 150),
    simulateTask("Analytics-Stream", 300)
  ];

  const results = await Promise.all(tasks);
  results.forEach(res => console.log(res));
  console.log("🎉 All 4 pipeline stages executed synchronously in parallel!");
}

runPipeline();
'''
    write_workspace_file("async_pipeline.js", node_code)

    # 4. Buggy Python sample (for quick debugging demonstration)
    buggy_code = '''# DevPulse AI - Deliberate Bug Test Case
# Click "Run Code", then click "Debug with AI" to see the agent fix this instantly!

def process_user_records(records):
    total_score = 0
    # BUG: Attempting to access key that doesn't exist for all records without checking
    # or dividing by zero if list is empty
    for user in records:
        print(f"Processing {user['name']}...")
        total_score += user["score"]
        
    avg = total_score / len(records)
    return avg

users = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie"} # Missing 'score' key! Raises KeyError
]

print("Average Score:", process_user_records(users))
'''
    write_workspace_file("buggy_sample.py", buggy_code)
