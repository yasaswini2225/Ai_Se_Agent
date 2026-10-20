// Web Audio Synthesizer
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
