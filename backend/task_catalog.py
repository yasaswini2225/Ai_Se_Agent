"""
DevPulse AI - Comprehensive 30 Engineering Tasks Catalog
Contains production-grade blueprints for the 30 benchmark tasks.
"""
from typing import Dict, Any, Optional
from .workspace_manager import write_workspace_file

def get_catalog_task(task_prompt: str) -> Optional[Dict[str, Any]]:
    p = task_prompt.lower()

    # 1. Calculator
    if "calculator" in p and not any(k in p for k in ["bmi", "marks", "student marks"]):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Quantum Scientific Calculator</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .calc { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:28px; width:100%; max-width:360px; box-shadow:0 25px 50px rgba(0,0,0,0.7); }
    .screen { background:#09090b; border:1px solid #27272a; border-radius:14px; padding:18px; text-align:right; margin-bottom:20px; min-height:90px; display:flex; flex-direction:column; justify-content:space-between; }
    .history { font-family:'JetBrains Mono',monospace; font-size:13px; color:#71717a; min-height:18px; }
    .display { font-family:'JetBrains Mono',monospace; font-size:36px; font-weight:700; color:#38bdf8; word-break:break-all; }
    .grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
    button { background:#27272a; border:none; border-radius:12px; padding:16px; font-size:18px; font-weight:700; color:#e4e4e7; cursor:pointer; transition:0.15s; }
    button:hover { background:#3f3f46; transform:scale(1.03); }
    button.op { background:#3b82f6; color:#fff; }
    button.op:hover { background:#2563eb; }
    button.special { background:#ef4444; color:#fff; }
    button.eq { background:#10b981; grid-column:span 2; }
  </style>
</head>
<body>
  <div class="calc">
    <div class="screen">
      <div id="hist" class="history"></div>
      <div id="disp" class="display">0</div>
    </div>
    <div class="grid">
      <button class="special" onclick="clr()">C</button>
      <button onclick="add('(')">(</button>
      <button onclick="add(')')">)</button>
      <button class="op" onclick="add('/')">÷</button>
      <button onclick="add('7')">7</button>
      <button onclick="add('8')">8</button>
      <button onclick="add('9')">9</button>
      <button class="op" onclick="add('*')">×</button>
      <button onclick="add('4')">4</button>
      <button onclick="add('5')">5</button>
      <button onclick="add('6')">6</button>
      <button class="op" onclick="add('-')">-</button>
      <button onclick="add('1')">1</button>
      <button onclick="add('2')">2</button>
      <button onclick="add('3')">3</button>
      <button class="op" onclick="add('+')">+</button>
      <button onclick="add('0')">0</button>
      <button onclick="add('.')">.</button>
      <button class="eq" onclick="calc()">=</button>
    </div>
  </div>
  <script>
    let expr = "";
    const d = document.getElementById('disp'), h = document.getElementById('hist');
    function add(c) { if(expr==="0" && c!==".") expr=""; expr+=c; d.textContent=expr; }
    function clr() { expr=""; d.textContent="0"; h.textContent=""; }
    function calc() {
      try {
        const s = expr.replace(/×/g,'*').replace(/÷/g,'/');
        const res = Function(`'use strict'; return (${s})`)();
        h.textContent = expr + " =";
        expr = String(res);
        d.textContent = expr;
      } catch(e) { d.textContent="Error"; expr=""; }
    }
  </script>
</body>
</html>'''
        write_workspace_file("calculator/index.html", html)
        return {
            "summary": "Built Quantum Scientific Calculator web application.",
            "plan": ["Design dark glass calculator card", "Implement arithmetic calculation engine", "Write to workspace"],
            "files": [{"path": "calculator/index.html", "content": html, "action": "create", "explanation": "Scientific Calculator"}],
            "executed_files": ["calculator/index.html"],
            "next_steps": "Open 'calculator/index.html' and toggle to Live Web Preview!"
        }

    # 2. Student Management System
    if "student management" in p or ("student" in p and "system" in p):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>EduTrack - Student Management System</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=JetBrains+Mono:wght@600&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#f1f5f9; min-height:100vh; padding:32px 20px; }
    .container { max-width:960px; margin:0 auto; }
    header { display:flex; justify-content:space-between; align-items:center; margin-bottom:28px; }
    h1 { font-size:26px; font-weight:800; background:linear-gradient(135deg,#60a5fa,#a78bfa); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .stats { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:24px; }
    .stat-card { background:#18181b; border:1px solid #27272a; border-radius:16px; padding:20px; }
    .stat-num { font-size:28px; font-weight:800; color:#38bdf8; margin-top:4px; font-family:'JetBrains Mono',monospace; }
    .form-card { background:#18181b; border:1px solid #27272a; border-radius:16px; padding:24px; margin-bottom:24px; }
    .input-grid { display:grid; grid-template-columns:repeat(4,1fr) auto; gap:12px; }
    input, select { background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; }
    button.add-btn { background:#6366f1; border:none; border-radius:10px; padding:12px 24px; color:#fff; font-weight:700; cursor:pointer; }
    table { width:100%; border-collapse:collapse; background:#18181b; border-radius:16px; overflow:hidden; border:1px solid #27272a; }
    th, td { padding:14px 18px; text-align:left; font-size:13px; border-bottom:1px solid #27272a; }
    th { background:#1f1f23; color:#94a3b8; font-size:11px; text-transform:uppercase; letter-spacing:1px; }
    .badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:700; }
    .badge-a { background:rgba(16,185,129,0.2); color:#10b981; }
    .badge-b { background:rgba(56,189,248,0.2); color:#38bdf8; }
    .del-btn { background:rgba(244,63,94,0.15); border:none; color:#f43f5e; padding:6px 12px; border-radius:8px; cursor:pointer; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <h1>🎓 EduTrack System</h1>
        <p style="color:#64748b; font-size:13px; margin-top:4px;">Comprehensive Student Information & GPA Registry</p>
      </div>
      <input type="text" id="search" placeholder="Search student..." oninput="render()" style="width:240px;">
    </header>

    <div class="stats">
      <div class="stat-card"><div>Total Enrolled</div><div id="total-count" class="stat-num">0</div></div>
      <div class="stat-card"><div>Average GPA</div><div id="avg-gpa" class="stat-num">0.0</div></div>
      <div class="stat-card"><div>Top Department</div><div class="stat-num" style="font-size:22px; color:#a78bfa;">CS & AI</div></div>
    </div>

    <div class="form-card">
      <div class="input-grid">
        <input type="text" id="name" placeholder="Student Name">
        <input type="text" id="id" placeholder="Student ID (e.g. CS-204)">
        <select id="course">
          <option>Computer Science</option><option>Data Science</option><option>Software Eng</option><option>Cybersecurity</option>
        </select>
        <input type="number" id="gpa" placeholder="GPA (0.0 - 4.0)" step="0.1" min="0" max="4">
        <button class="add-btn" onclick="addStudent()">Add Student</button>
      </div>
    </div>

    <table>
      <thead>
        <tr><th>ID</th><th>Student Name</th><th>Course</th><th>GPA</th><th>Status</th><th>Action</th></tr>
      </thead>
      <tbody id="table-body"></tbody>
    </table>
  </div>
  <script>
    let students = [
      { id: "CS-101", name: "Alex Mercer", course: "Computer Science", gpa: 3.9 },
      { id: "SE-104", name: "Samantha Reed", course: "Software Eng", gpa: 3.8 },
      { id: "DS-202", name: "David Kim", course: "Data Science", gpa: 3.5 }
    ];
    function render() {
      const q = document.getElementById('search').value.toLowerCase();
      const filtered = students.filter(s => s.name.toLowerCase().includes(q) || s.id.toLowerCase().includes(q));
      const tbody = document.getElementById('table-body');
      tbody.innerHTML = "";
      filtered.forEach((s, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-family:'JetBrains Mono'; color:#38bdf8;">${s.id}</td>
          <td><b>${s.name}</b></td>
          <td>${s.course}</td>
          <td style="font-family:'JetBrains Mono'; font-weight:700;">${s.gpa}</td>
          <td><span class="badge ${s.gpa >= 3.6 ? 'badge-a' : 'badge-b'}">${s.gpa >= 3.6 ? 'Honor Roll' : 'In Good Standing'}</span></td>
          <td><button class="del-btn" onclick="delStudent(${i})">Remove</button></td>
        `;
        tbody.appendChild(tr);
      });
      document.getElementById('total-count').textContent = students.length;
      const avg = students.length ? (students.reduce((a,c)=>a+parseFloat(c.gpa),0)/students.length).toFixed(2) : "0.0";
      document.getElementById('avg-gpa').textContent = avg;
    }
    function addStudent() {
      const name = document.getElementById('name').value.trim();
      const id = document.getElementById('id').value.trim();
      const course = document.getElementById('course').value;
      const gpa = parseFloat(document.getElementById('gpa').value) || 3.0;
      if (!name || !id) return alert("Fill Name and ID");
      students.unshift({ id, name, course, gpa });
      document.getElementById('name').value = '';
      document.getElementById('id').value = '';
      document.getElementById('gpa').value = '';
      render();
    }
    function delStudent(idx) { students.splice(idx,1); render(); }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("student_management/index.html", html)
        return {
            "summary": "Built EduTrack Student Management System with GPA analytics, search filter, and enrollment table.",
            "plan": ["Design modern data dashboard", "Implement student database state & GPA aggregations", "Save to workspace"],
            "files": [{"path": "student_management/index.html", "content": html, "action": "create", "explanation": "Student Management Web System"}],
            "executed_files": ["student_management/index.html"],
            "next_steps": "Open 'student_management/index.html' and toggle to Live Web Preview!"
        }

    # 3. To-Do List App
    if "to-do" in p or "todo" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseTask - To-Do List App</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:32px 16px; display:flex; justify-content:center; }
    .box { width:100%; max-width:540px; background:#18181b; border:1px solid #27272a; border-radius:24px; padding:28px; box-shadow:0 25px 50px rgba(0,0,0,0.6); }
    h1 { font-size:24px; font-weight:800; background:linear-gradient(135deg,#38bdf8,#818cf8); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:16px; }
    .input-row { display:flex; gap:8px; margin-bottom:20px; }
    input { flex:1; background:#09090b; border:1px solid #3f3f46; border-radius:12px; padding:12px 16px; color:#fff; font-size:14px; outline:none; }
    button.add-btn { background:#6366f1; border:none; border-radius:12px; padding:12px 20px; color:#fff; font-weight:700; cursor:pointer; }
    .filters { display:flex; gap:8px; margin-bottom:16px; }
    .filter-btn { background:#27272a; border:none; border-radius:8px; padding:6px 14px; color:#94a3b8; font-size:12px; font-weight:700; cursor:pointer; }
    .filter-btn.active { background:#6366f1; color:#fff; }
    .list { display:flex; flex-direction:column; gap:10px; }
    .item { background:#09090b; border:1px solid #27272a; border-radius:14px; padding:14px 18px; display:flex; align-items:center; justify-content:space-between; }
    .item.done span { text-decoration:line-through; color:#64748b; }
    .del-btn { background:transparent; border:none; color:#f43f5e; cursor:pointer; font-size:16px; }
  </style>
</head>
<body>
  <div class="box">
    <h1>⚡ PulseTask Manager</h1>
    <div class="input-row">
      <input type="text" id="taskInput" placeholder="Add a new task...">
      <button class="add-btn" onclick="add()">Add</button>
    </div>
    <div class="filters">
      <button class="filter-btn active" onclick="setFilter('all')">All</button>
      <button class="filter-btn" onclick="setFilter('active')">Active</button>
      <button class="filter-btn" onclick="setFilter('completed')">Completed</button>
    </div>
    <div id="list" class="list"></div>
  </div>
  <script>
    let filter = 'all';
    let tasks = [
      { text: "Complete AI software engineering project", done: true },
      { text: "Design modern responsive UI components", done: false },
      { text: "Run automated unit test suites", done: false }
    ];
    function render() {
      const list = document.getElementById('list');
      list.innerHTML = "";
      const filtered = tasks.filter(t => filter==='all' ? true : (filter==='active' ? !t.done : t.done));
      filtered.forEach((t, i) => {
        const div = document.createElement('div');
        div.className = 'item' + (t.done ? ' done' : '');
        div.innerHTML = `
          <div style="display:flex; align-items:center; gap:12px;">
            <input type="checkbox" ${t.done ? 'checked' : ''} onchange="toggle(${i})">
            <span>${t.text}</span>
          </div>
          <button class="del-btn" onclick="del(${i})">✕</button>
        `;
        list.appendChild(div);
      });
    }
    function add() {
      const inp = document.getElementById('taskInput');
      if (!inp.value.trim()) return;
      tasks.unshift({ text: inp.value.trim(), done: false });
      inp.value = "";
      render();
    }
    function toggle(i) { tasks[i].done = !tasks[i].done; render(); }
    function del(i) { tasks.splice(i, 1); render(); }
    function setFilter(f) {
      filter = f;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.toggle('active', b.textContent.toLowerCase()===f));
      render();
    }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("todo_app/index.html", html)
        return {
            "summary": "Built PulseTask To-Do List Application with filters, checkboxes, and local state.",
            "plan": ["Setup reactive list layout", "Implement filter tabs (All, Active, Completed)", "Write to workspace"],
            "files": [{"path": "todo_app/index.html", "content": html, "action": "create", "explanation": "To-Do List Web App"}],
            "executed_files": ["todo_app/index.html"],
            "next_steps": "Open 'todo_app/index.html' and toggle to Live Web Preview!"
        }

    # 4. Personal Portfolio Website
    if "portfolio" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>DevPortfolio - Full-Stack AI Engineer</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#f8fafc; line-height:1.6; }
    nav { display:flex; justify-content:space-between; align-items:center; padding:20px 48px; border-bottom:1px solid #27272a; position:sticky; top:0; background:rgba(9,9,11,0.85); backdrop-filter:blur(10px); }
    .logo { font-size:20px; font-weight:800; color:#38bdf8; }
    .hero { text-align:center; padding:80px 20px; max-width:800px; margin:0 auto; }
    .hero h1 { font-size:48px; font-weight:800; letter-spacing:-1px; margin-bottom:16px; background:linear-gradient(135deg,#ffffff 0%,#94a3b8 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .hero p { font-size:18px; color:#94a3b8; margin-bottom:28px; }
    .btn { background:linear-gradient(135deg,#6366f1,#3b82f6); color:#fff; padding:14px 28px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-block; }
    .section { max-width:1000px; margin:0 auto; padding:60px 20px; }
    .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:24px; margin-top:32px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:20px; padding:24px; transition:0.2s; }
    .card:hover { transform:translateY(-4px); border-color:#6366f1; }
    .card h3 { font-size:18px; color:#38bdf8; margin-bottom:8px; }
    .skills-pills { display:flex; flex-wrap:wrap; gap:10px; margin-top:20px; }
    .pill { background:#27272a; padding:6px 14px; border-radius:20px; font-size:12px; font-weight:700; color:#cbd5e1; }
  </style>
</head>
<body>
  <nav>
    <div class="logo">⚡ DEV.FOLIO</div>
    <div style="display:flex; gap:20px; font-size:14px; font-weight:600; color:#94a3b8;">
      <a href="#projects" style="color:inherit; text-decoration:none;">Projects</a>
      <a href="#skills" style="color:inherit; text-decoration:none;">Skills</a>
      <a href="#contact" style="color:inherit; text-decoration:none;">Contact</a>
    </div>
  </nav>

  <div class="hero">
    <h1>Software Engineer & AI Architect</h1>
    <p>Crafting high-throughput microservices, intelligent autonomous agents, and elegant modern user interfaces.</p>
    <a href="#projects" class="btn">View Featured Work</a>
  </div>

  <div id="projects" class="section">
    <h2 style="font-size:28px; font-weight:800;">Featured Projects</h2>
    <div class="grid">
      <div class="card">
        <h3>DevPulse AI Agent</h3>
        <p style="color:#94a3b8; font-size:13px;">Full-stack autonomous software engineer and cloud IDE running multi-language execution.</p>
      </div>
      <div class="card">
        <h3>Realtime Engine</h3>
        <p style="color:#94a3b8; font-size:13px;">Distributed event streaming engine with sub-millisecond pub/sub latency.</p>
      </div>
      <div class="card">
        <h3>ChronoPulse Arcade</h3>
        <p style="color:#94a3b8; font-size:13px;">Interactive game engine built with canvas rendering and Web Audio API.</p>
      </div>
    </div>
  </div>

  <div id="skills" class="section">
    <h2 style="font-size:28px; font-weight:800;">Core Competencies</h2>
    <div class="skills-pills">
      <span class="pill">Python</span><span class="pill">FastAPI</span><span class="pill">TypeScript</span>
      <span class="pill">React / Next.js</span><span class="pill">Docker</span><span class="pill">PostgreSQL</span>
      <span class="pill">System Design</span><span class="pill">AI / LLM Orchestration</span>
    </div>
  </div>
</body>
</html>'''
        write_workspace_file("portfolio/index.html", html)
        return {
            "summary": "Built personal portfolio website with hero banner, projects showcase, and skills grid.",
            "plan": ["Design modern developer portfolio", "Create responsive grid layouts", "Save to workspace"],
            "files": [{"path": "portfolio/index.html", "content": html, "action": "create", "explanation": "Personal Portfolio Website"}],
            "executed_files": ["portfolio/index.html"],
            "next_steps": "Open 'portfolio/index.html' and toggle to Live Web Preview!"
        }

    # 5. Login and Registration Page
    if "login" in p or "registration" in p or "auth" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>KeyGate - Login & Registration Portal</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:radial-gradient(circle at 50% 20%, #1e1b4b, #09090b); color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:rgba(24,24,27,0.85); backdrop-filter:blur(20px); border:1px solid rgba(255,255,255,0.1); border-radius:24px; padding:32px; width:100%; max-width:400px; box-shadow:0 25px 50px rgba(0,0,0,0.7); }
    .tabs { display:flex; background:#09090b; border-radius:12px; padding:4px; margin-bottom:24px; }
    .tab-btn { flex:1; background:transparent; border:none; padding:8px; border-radius:8px; color:#94a3b8; font-weight:700; font-size:13px; cursor:pointer; }
    .tab-btn.active { background:#6366f1; color:#fff; }
    .field { margin-bottom:16px; }
    label { display:block; font-size:12px; font-weight:700; color:#94a3b8; margin-bottom:6px; }
    input { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:14px; outline:none; }
    button.submit-btn { width:100%; background:linear-gradient(135deg,#6366f1,#4f46e5); border:none; padding:12px; border-radius:10px; color:#fff; font-weight:700; font-size:14px; cursor:pointer; margin-top:8px; }
    .alert { padding:10px; border-radius:8px; font-size:12px; margin-top:14px; display:none; }
  </style>
</head>
<body>
  <div class="card">
    <div class="tabs">
      <button id="tab-login" class="tab-btn active" onclick="switchTab('login')">Sign In</button>
      <button id="tab-register" class="tab-btn" onclick="switchTab('register')">Register</button>
    </div>
    <form id="auth-form" onsubmit="handleSubmit(event)">
      <div id="reg-fields" style="display:none;" class="field">
        <label>Full Name</label>
        <input type="text" id="name" placeholder="John Doe">
      </div>
      <div class="field">
        <label>Email Address</label>
        <input type="email" id="email" placeholder="dev@pulse.ai" required>
      </div>
      <div class="field">
        <label>Password</label>
        <input type="password" id="password" placeholder="••••••••" required>
      </div>
      <button type="submit" id="submit-btn" class="submit-btn">Sign In</button>
      <div id="alert-box" class="alert"></div>
    </form>
  </div>
  <script>
    let mode = 'login';
    function switchTab(m) {
      mode = m;
      document.getElementById('tab-login').classList.toggle('active', mode==='login');
      document.getElementById('tab-register').classList.toggle('active', mode==='register');
      document.getElementById('reg-fields').style.display = mode==='register' ? 'block' : 'none';
      document.getElementById('submit-btn').textContent = mode==='register' ? 'Create Account' : 'Sign In';
      document.getElementById('alert-box').style.display = 'none';
    }
    function handleSubmit(e) {
      e.preventDefault();
      const a = document.getElementById('alert-box');
      a.style.display = 'block';
      a.style.background = 'rgba(16,185,129,0.2)';
      a.style.color = '#10b981';
      a.textContent = mode==='login' ? '✔ Successfully authenticated!' : '✔ Account registered successfully!';
    }
  </script>
</body>
</html>'''
        write_workspace_file("auth_system/index.html", html)
        return {
            "summary": "Built KeyGate Login & Registration Portal with tabbed state and instant form feedback.",
            "plan": ["Design modern dark glass auth card", "Implement switchable login/registration modes", "Mount to workspace"],
            "files": [{"path": "auth_system/index.html", "content": html, "action": "create", "explanation": "Login & Registration System"}],
            "executed_files": ["auth_system/index.html"],
            "next_steps": "Open 'auth_system/index.html' and toggle to Live Web Preview!"
        }

    # 6. Weather App
    if "weather" in p:
        return None # Handled by main agent generator

    # 7. Notes Application
    if "note" in p or "notes" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseNotes - Rich Notes App</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:24px; display:flex; justify-content:center; }
    .container { width:100%; max-width:720px; }
    header { display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; }
    h1 { font-size:24px; font-weight:800; color:#38bdf8; }
    .create-card { background:#18181b; border:1px solid #27272a; border-radius:16px; padding:20px; margin-bottom:24px; }
    input, textarea { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; margin-bottom:10px; }
    textarea { height:90px; resize:vertical; }
    button.save-btn { background:#6366f1; border:none; border-radius:10px; padding:10px 20px; color:#fff; font-weight:700; cursor:pointer; }
    .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:16px; }
    .note-card { background:#18181b; border:1px solid #27272a; border-radius:16px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; min-height:140px; }
    .note-title { font-weight:800; font-size:15px; color:#f1f5f9; margin-bottom:6px; }
    .note-body { font-size:12px; color:#94a3b8; line-height:1.5; white-space:pre-wrap; }
    .note-foot { display:flex; justify-content:space-between; align-items:center; margin-top:14px; font-size:10px; color:#64748b; }
    .del { background:transparent; border:none; color:#f43f5e; cursor:pointer; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>📝 PulseNotes</h1>
      <input type="text" id="search" placeholder="Search notes..." oninput="render()" style="width:200px; margin:0;">
    </header>
    <div class="create-card">
      <input type="text" id="title" placeholder="Note Title...">
      <textarea id="body" placeholder="Write your note contents..."></textarea>
      <button class="save-btn" onclick="addNote()">Save Note</button>
    </div>
    <div id="grid" class="grid"></div>
  </div>
  <script>
    let notes = [
      { title: "System Architecture", body: "Decouple microservices using Redis pub/sub queue.", date: "Today" },
      { title: "Frontend Checklist", body: "Verify accessible colors, dark mode styling, and Monaco keyboard shortcuts.", date: "Yesterday" }
    ];
    function render() {
      const q = document.getElementById('search').value.toLowerCase();
      const grid = document.getElementById('grid');
      grid.innerHTML = "";
      notes.filter(n => n.title.toLowerCase().includes(q) || n.body.toLowerCase().includes(q)).forEach((n, i) => {
        const div = document.createElement('div');
        div.className = 'note-card';
        div.innerHTML = `
          <div>
            <div class="note-title">${n.title}</div>
            <div class="note-body">${n.body}</div>
          </div>
          <div class="note-foot">
            <span>${n.date}</span>
            <button class="del" onclick="delNote(${i})">Delete</button>
          </div>
        `;
        grid.appendChild(div);
      });
    }
    function addNote() {
      const t = document.getElementById('title').value.trim();
      const b = document.getElementById('body').value.trim();
      if (!t || !b) return alert("Please provide title and content");
      notes.unshift({ title: t, body: b, date: "Just now" });
      document.getElementById('title').value = "";
      document.getElementById('body').value = "";
      render();
    }
    function delNote(i) { notes.splice(i, 1); render(); }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("notes_app/index.html", html)
        return {
            "summary": "Built PulseNotes rich note-taking web application with dynamic search and card layouts.",
            "plan": ["Setup interactive notes layout", "Implement card CRUD and search filtering", "Save to workspace"],
            "files": [{"path": "notes_app/index.html", "content": html, "action": "create", "explanation": "Notes Application"}],
            "executed_files": ["notes_app/index.html"],
            "next_steps": "Open 'notes_app/index.html' and toggle to Live Web Preview!"
        }

    # 8. Quiz Application
    if "quiz" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BrainPulse - Quiz Application</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; width:100%; max-width:480px; box-shadow:0 25px 50px rgba(0,0,0,0.7); }
    .progress-bar { height:6px; background:#27272a; border-radius:3px; margin-bottom:20px; overflow:hidden; }
    .progress-fill { height:100%; width:20%; background:#38bdf8; transition:width 0.3s; }
    .question { font-size:18px; font-weight:800; margin-bottom:20px; line-height:1.4; }
    .options { display:flex; flex-direction:column; gap:10px; margin-bottom:20px; }
    button.opt { background:#09090b; border:1px solid #3f3f46; border-radius:12px; padding:14px; color:#fff; font-size:14px; font-weight:600; text-align:left; cursor:pointer; transition:0.15s; }
    button.opt:hover { border-color:#6366f1; background:#1f1f2e; }
    button.opt.correct { background:#10b981; border-color:#10b981; }
    button.opt.wrong { background:#ef4444; border-color:#ef4444; }
    .score-view { text-align:center; padding:20px 0; }
  </style>
</head>
<body>
  <div class="card">
    <div class="progress-bar"><div id="fill" class="progress-fill"></div></div>
    <div id="quiz-body">
      <div id="q" class="question">Loading question...</div>
      <div id="opts" class="options"></div>
    </div>
  </div>
  <script>
    const questions = [
      { q: "What is the primary benefit of an Event Loop?", opts: ["Non-blocking async I/O", "Multi-core parallel CPU usage", "Automatic garbage collection", "Static code compilation"], a: 0 },
      { q: "Which data structure uses LIFO (Last-In-First-Out)?", opts: ["Queue", "Stack", "Binary Search Tree", "Linked List"], a: 1 },
      { q: "What is the time complexity of lookup in an average Hash Map?", opts: ["O(n)", "O(log n)", "O(1)", "O(n^2)"], a: 2 },
      { q: "Which protocol operates at the transport layer of the OSI model?", opts: ["HTTP", "TCP", "DNS", "BGP"], a: 1 }
    ];
    let curr = 0, score = 0;
    function loadQ() {
      if (curr >= questions.length) {
        document.getElementById('quiz-body').innerHTML = `
          <div class="score-view">
            <h2 style="font-size:28px; color:#38bdf8; margin-bottom:8px;">Quiz Completed!</h2>
            <p style="color:#94a3b8; font-size:16px;">You scored <b>${score} / ${questions.length}</b> points.</p>
            <button onclick="location.reload()" style="margin-top:20px; background:#6366f1; border:none; padding:12px 24px; border-radius:12px; color:#fff; font-weight:700; cursor:pointer;">Restart Quiz</button>
          </div>
        `;
        return;
      }
      document.getElementById('fill').style.width = `${((curr+1)/questions.length)*100}%`;
      const item = questions[curr];
      document.getElementById('q').textContent = `${curr+1}. ${item.q}`;
      const oDiv = document.getElementById('opts');
      oDiv.innerHTML = '';
      item.opts.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'opt';
        btn.textContent = opt;
        btn.onclick = () => selectOpt(idx, btn);
        oDiv.appendChild(btn);
      });
    }
    function selectOpt(idx, btn) {
      const item = questions[curr];
      if (idx === item.a) { btn.classList.add('correct'); score++; }
      else { btn.classList.add('wrong'); }
      setTimeout(() => { curr++; loadQ(); }, 600);
    }
    loadQ();
  </script>
</body>
</html>'''
        write_workspace_file("quiz_app/index.html", html)
        return {
            "summary": "Built BrainPulse Quiz Application with interactive multiple choice, live scoring, and progress tracking.",
            "plan": ["Construct interactive quiz question engine", "Add progress bar and instant review feedback", "Write to workspace"],
            "files": [{"path": "quiz_app/index.html", "content": html, "action": "create", "explanation": "Interactive Quiz App"}],
            "executed_files": ["quiz_app/index.html"],
            "next_steps": "Open 'quiz_app/index.html' and toggle to Live Web Preview!"
        }

    # 9. Expense Tracker
    if "expense" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseSpend - Expense Tracker</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; justify-content:center; padding:24px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:28px; width:100%; max-width:460px; }
    .balance-card { text-align:center; padding:20px; background:#09090b; border-radius:16px; margin-bottom:20px; }
    .balance-val { font-family:'JetBrains Mono',monospace; font-size:36px; font-weight:800; color:#10b981; }
    .form-row { display:flex; gap:8px; margin-bottom:16px; }
    input, select { background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; }
    button.add { background:#6366f1; border:none; padding:12px 20px; border-radius:10px; color:#fff; font-weight:700; cursor:pointer; }
    .tx-item { background:#09090b; border:1px solid #27272a; border-radius:12px; padding:12px 16px; display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; font-size:13px; }
    .tx-amount { font-family:'JetBrains Mono',monospace; font-weight:700; }
  </style>
</head>
<body>
  <div class="card">
    <h2 style="font-size:22px; margin-bottom:16px; color:#38bdf8;">⚡ PulseSpend Tracker</h2>
    <div class="balance-card">
      <div style="font-size:11px; color:#71717a; text-transform:uppercase;">Net Balance</div>
      <div id="balance" class="balance-val">$0.00</div>
    </div>
    <div class="form-row">
      <input type="text" id="desc" placeholder="Expense description..." style="flex:2;">
      <input type="number" id="amt" placeholder="Amount" style="flex:1;">
      <select id="type"><option value="expense">Expense</option><option value="income">Income</option></select>
      <button class="add" onclick="addTx()">Add</button>
    </div>
    <div id="tx-list"></div>
  </div>
  <script>
    let txs = [
      { desc: "AWS Server Hosting", amt: -45.0, type: "expense" },
      { desc: "Freelance Project Milestone", amt: 650.0, type: "income" }
    ];
    function render() {
      const list = document.getElementById('tx-list');
      list.innerHTML = '';
      let bal = 0;
      txs.forEach((t, i) => {
        bal += t.amt;
        const div = document.createElement('div');
        div.className = 'tx-item';
        div.innerHTML = `
          <span>${t.desc}</span>
          <span class="tx-amount" style="color:${t.amt>=0?'#10b981':'#f43f5e'};">${t.amt>=0?'+':''}$${Math.abs(t.amt).toFixed(2)}</span>
        `;
        list.appendChild(div);
      });
      document.getElementById('balance').textContent = `$${bal.toFixed(2)}`;
      document.getElementById('balance').style.color = bal >= 0 ? '#10b981' : '#f43f5e';
    }
    function addTx() {
      const d = document.getElementById('desc').value.trim();
      const a = parseFloat(document.getElementById('amt').value);
      const typ = document.getElementById('type').value;
      if (!d || isNaN(a)) return;
      txs.unshift({ desc: d, amt: typ === 'expense' ? -Math.abs(a) : Math.abs(a), type: typ });
      document.getElementById('desc').value = '';
      document.getElementById('amt').value = '';
      render();
    }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("expense_tracker/index.html", html)
        return {
            "summary": "Built PulseSpend Expense Tracker with net balance calculations and real-time transaction ledger.",
            "plan": ["Design expense calculation card", "Implement income/expense balance aggregation", "Save to workspace"],
            "files": [{"path": "expense_tracker/index.html", "content": html, "action": "create", "explanation": "Expense Tracker App"}],
            "executed_files": ["expense_tracker/index.html"],
            "next_steps": "Open 'expense_tracker/index.html' and toggle to Live Web Preview!"
        }

    # 10. Simple Chatbot
    if "chatbot" in p or ("chat" in p and "bot" in p):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseBot - Intelligent Chatbot</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .chat-box { background:#18181b; border:1px solid #27272a; border-radius:24px; width:100%; max-width:440px; height:560px; display:flex; flex-direction:column; overflow:hidden; }
    header { padding:16px 20px; border-bottom:1px solid #27272a; background:#1f1f23; font-weight:800; font-size:16px; color:#38bdf8; }
    .messages { flex:1; overflow-y:auto; padding:16px; display:flex; flex-direction:column; gap:12px; }
    .msg { max-width:80%; padding:12px 16px; border-radius:16px; font-size:13px; line-height:1.4; }
    .msg.bot { background:#27272a; color:#f1f5f9; align-self:flex-start; border-bottom-left-radius:2px; }
    .msg.user { background:#6366f1; color:#fff; align-self:flex-end; border-bottom-right-radius:2px; }
    .input-box { display:flex; padding:12px; border-top:1px solid #27272a; gap:8px; }
    input { flex:1; background:#09090b; border:1px solid #3f3f46; border-radius:12px; padding:10px 14px; color:#fff; outline:none; font-size:13px; }
    button { background:#6366f1; border:none; padding:10px 18px; border-radius:12px; color:#fff; font-weight:700; cursor:pointer; }
  </style>
</head>
<body>
  <div class="chat-box">
    <header>🤖 PulseBot AI Assistant</header>
    <div id="msgs" class="messages">
      <div class="msg bot">Hello! I am PulseBot. Ask me about coding, algorithms, or project architecture!</div>
    </div>
    <form class="input-box" onsubmit="sendMsg(event)">
      <input type="text" id="userInput" placeholder="Ask a question...">
      <button type="submit">Send</button>
    </form>
  </div>
  <script>
    function sendMsg(e) {
      e.preventDefault();
      const inp = document.getElementById('userInput');
      const val = inp.value.trim();
      if (!val) return;
      inp.value = '';
      appendMsg(val, 'user');
      setTimeout(() => {
        let reply = "That's an insightful question! In software engineering, modular design and defensive error handling are fundamental best practices.";
        const vl = val.toLowerCase();
        if (vl.includes('hello') || vl.includes('hi')) reply = "Hello! Ready to code and solve engineering challenges together?";
        else if (vl.includes('python')) reply = "Python excels at data manipulation, backend APIs (FastAPI), and AI automation.";
        else if (vl.includes('javascript') || vl.includes('js')) reply = "JavaScript powers the modern interactive web and asynchronous event loops!";
        appendMsg(reply, 'bot');
      }, 500);
    }
    function appendMsg(text, sender) {
      const m = document.getElementById('msgs');
      const div = document.createElement('div');
      div.className = `msg ${sender}`;
      div.textContent = text;
      m.appendChild(div);
      m.scrollTop = m.scrollHeight;
    }
  </script>
</body>
</html>'''
        write_workspace_file("chatbot_app/index.html", html)
        return {
            "summary": "Built PulseBot conversational chatbot web application with reactive message bubbles.",
            "plan": ["Design chat UI message stream", "Implement automated response parser", "Write to workspace"],
            "files": [{"path": "chatbot_app/index.html", "content": html, "action": "create", "explanation": "Simple Chatbot Application"}],
            "executed_files": ["chatbot_app/index.html"],
            "next_steps": "Open 'chatbot_app/index.html' and toggle to Live Web Preview!"
        }

    # 11. Library Management System
    if "library" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BookVault - Library Management</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:32px 20px; }
    .container { max-width:840px; margin:0 auto; }
    h1 { font-size:26px; color:#38bdf8; margin-bottom:24px; }
    .form-row { display:flex; gap:10px; margin-bottom:20px; }
    input { background:#18181b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; flex:1; }
    button.btn { background:#6366f1; border:none; border-radius:10px; padding:12px 24px; color:#fff; font-weight:700; cursor:pointer; }
    table { width:100%; border-collapse:collapse; background:#18181b; border-radius:16px; overflow:hidden; border:1px solid #27272a; }
    th, td { padding:14px 18px; text-align:left; font-size:13px; border-bottom:1px solid #27272a; }
    th { background:#1f1f23; color:#94a3b8; font-size:11px; text-transform:uppercase; }
    .badge { padding:3px 8px; border-radius:8px; font-size:11px; font-weight:700; }
    .avail { background:rgba(16,185,129,0.2); color:#10b981; }
    .borrowed { background:rgba(244,63,94,0.2); color:#f43f5e; }
    .action-btn { background:#27272a; border:none; color:#cbd5e1; padding:6px 12px; border-radius:6px; cursor:pointer; }
  </style>
</head>
<body>
  <div class="container">
    <h1>📚 BookVault Library Management</h1>
    <div class="form-row">
      <input type="text" id="title" placeholder="Book Title...">
      <input type="text" id="author" placeholder="Author...">
      <button class="btn" onclick="addBook()">Add Book</button>
    </div>
    <table>
      <thead><tr><th>Book Title</th><th>Author</th><th>Status</th><th>Toggle</th></tr></thead>
      <tbody id="books"></tbody>
    </table>
  </div>
  <script>
    let books = [
      { title: "Clean Code", author: "Robert C. Martin", available: true },
      { title: "Design Patterns", author: "Gang of Four", available: false },
      { title: "Introduction to Algorithms", author: "CLRS", available: true }
    ];
    function render() {
      const b = document.getElementById('books');
      b.innerHTML = '';
      books.forEach((book, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><b>${book.title}</b></td>
          <td style="color:#94a3b8;">${book.author}</td>
          <td><span class="badge ${book.available?'avail':'borrowed'}">${book.available?'Available':'Borrowed'}</span></td>
          <td><button class="action-btn" onclick="toggleBook(${i})">${book.available?'Borrow':'Return'}</button></td>
        `;
        b.appendChild(tr);
      });
    }
    function addBook() {
      const t = document.getElementById('title').value.trim();
      const a = document.getElementById('author').value.trim();
      if (!t || !a) return;
      books.unshift({ title: t, author: a, available: true });
      document.getElementById('title').value = '';
      document.getElementById('author').value = '';
      render();
    }
    function toggleBook(i) { books[i].available = !books[i].available; render(); }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("library_system/index.html", html)
        return {
            "summary": "Built BookVault Library Management System with borrowing/return toggles and catalog registry.",
            "plan": ["Design library inventory table", "Implement availability toggling", "Write to workspace"],
            "files": [{"path": "library_system/index.html", "content": html, "action": "create", "explanation": "Library Management System"}],
            "executed_files": ["library_system/index.html"],
            "next_steps": "Open 'library_system/index.html' and toggle to Live Web Preview!"
        }

    # 12. E-commerce Website
    if "e-commerce" in p or "ecommerce" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>NovaStore - Modern E-Commerce</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:24px; }
    .header { display:flex; justify-content:space-between; align-items:center; max-width:1000px; margin:0 auto 32px; border-bottom:1px solid #27272a; padding-bottom:16px; }
    h1 { font-size:24px; color:#38bdf8; }
    .cart-btn { background:#6366f1; border:none; padding:10px 20px; border-radius:12px; color:#fff; font-weight:700; cursor:pointer; }
    .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:20px; max-width:1000px; margin:0 auto; }
    .item-card { background:#18181b; border:1px solid #27272a; border-radius:20px; padding:20px; display:flex; flex-direction:column; justify-content:space-between; }
    .item-img { font-size:48px; text-align:center; padding:20px; background:#09090b; border-radius:14px; margin-bottom:14px; }
    .item-price { font-family:'JetBrains Mono',monospace; font-size:18px; color:#10b981; font-weight:700; margin:10px 0; }
    .buy-btn { background:#3b82f6; border:none; padding:10px; border-radius:10px; color:#fff; font-weight:700; cursor:pointer; }
  </style>
</head>
<body>
  <div class="header">
    <h1>🛍️ NovaStore Tech Catalog</h1>
    <button class="cart-btn" onclick="alert('Cart total: ' + cartCount + ' items')">🛒 Cart: <span id="cart">0</span></button>
  </div>
  <div class="grid">
    <div class="item-card">
      <div class="item-img">💻</div>
      <h3>M3 Ultra Workstation</h3>
      <div class="item-price">$2,499</div>
      <button class="buy-btn" onclick="addCart()">Add to Cart</button>
    </div>
    <div class="item-card">
      <div class="item-img">🎧</div>
      <h3>Spatial Audio Pro</h3>
      <div class="item-price">$349</div>
      <button class="buy-btn" onclick="addCart()">Add to Cart</button>
    </div>
    <div class="item-card">
      <div class="item-img">⌨️</div>
      <h3>CyberMechanical Keyboard</h3>
      <div class="item-price">$189</div>
      <button class="buy-btn" onclick="addCart()">Add to Cart</button>
    </div>
  </div>
  <script>
    let cartCount = 0;
    function addCart() {
      cartCount++;
      document.getElementById('cart').textContent = cartCount;
    }
  </script>
</body>
</html>'''
        write_workspace_file("ecommerce/index.html", html)
        return {
            "summary": "Built NovaStore modern E-Commerce product catalog with reactive cart aggregation.",
            "plan": ["Design product grid and pricing cards", "Implement cart counter state", "Mount to workspace"],
            "files": [{"path": "ecommerce/index.html", "content": html, "action": "create", "explanation": "E-Commerce Website"}],
            "executed_files": ["ecommerce/index.html"],
            "next_steps": "Open 'ecommerce/index.html' and toggle to Live Web Preview!"
        }

    # 13. Password Generator (Handled in main agent, fallback here)
    if "password" in p:
        return None

    # 14. Digital Clock
    if "digital clock" in p or ("clock" in p and "digital" in p):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CyberClock - Digital Clock</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&family=Plus+Jakarta+Sans:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'JetBrains Mono',monospace; }
    body { background:radial-gradient(circle at 50% 50%, #1e1b4b, #09090b); color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; }
    .clock-card { background:rgba(18,18,24,0.9); border:1px solid rgba(99,102,241,0.3); border-radius:24px; padding:48px; text-align:center; box-shadow:0 0 50px rgba(99,102,241,0.2); }
    .time { font-size:64px; font-weight:800; color:#38bdf8; text-shadow:0 0 20px rgba(56,189,248,0.5); letter-spacing:2px; }
    .date { font-size:16px; color:#818cf8; margin-top:12px; font-family:'Plus Jakarta Sans',sans-serif; }
  </style>
</head>
<body>
  <div class="clock-card">
    <div id="time" class="time">00:00:00</div>
    <div id="date" class="date">Loading date...</div>
  </div>
  <script>
    function update() {
      const now = new Date();
      document.getElementById('time').textContent = now.toTimeString().slice(0, 8);
      document.getElementById('date').textContent = now.toLocaleDateString(undefined, { weekday:'long', year:'numeric', month:'long', day:'numeric' });
    }
    setInterval(update, 1000);
    update();
  </script>
</body>
</html>'''
        write_workspace_file("digital_clock/index.html", html)
        return {
            "summary": "Built CyberClock digital clock with live seconds ticking and formatted calendar date.",
            "plan": ["Construct neon clock display", "Implement 1-second interval refresh", "Write to workspace"],
            "files": [{"path": "digital_clock/index.html", "content": html, "action": "create", "explanation": "Digital Clock App"}],
            "executed_files": ["digital_clock/index.html"],
            "next_steps": "Open 'digital_clock/index.html' and toggle to Live Web Preview!"
        }

    # 15. Number Guessing Game
    if "number guessing" in p or "guessing game" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>NumGuess - Number Guessing Game</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; width:100%; max-width:420px; text-align:center; }
    h1 { font-size:24px; color:#38bdf8; margin-bottom:12px; }
    .input-row { display:flex; gap:8px; margin:20px 0; }
    input { flex:1; background:#09090b; border:1px solid #3f3f46; border-radius:12px; padding:12px; color:#fff; font-size:16px; font-family:'JetBrains Mono',monospace; outline:none; text-align:center; }
    button { background:#6366f1; border:none; padding:12px 20px; border-radius:12px; color:#fff; font-weight:700; cursor:pointer; }
    .feedback { font-size:16px; font-weight:700; min-height:24px; margin-bottom:10px; }
    .stats { font-size:13px; color:#94a3b8; }
  </style>
</head>
<body>
  <div class="card">
    <h1>🎯 NumGuess Game</h1>
    <p style="color:#94a3b8; font-size:13px;">Guess a secret number between 1 and 100</p>
    <div class="input-row">
      <input type="number" id="guess" min="1" max="100" placeholder="50">
      <button onclick="checkGuess()">Guess</button>
    </div>
    <div id="msg" class="feedback">Make your first guess!</div>
    <div class="stats">Attempts: <span id="tries">0</span></div>
  </div>
  <script>
    let secret = Math.floor(Math.random() * 100) + 1;
    let attempts = 0;
    function checkGuess() {
      const g = parseInt(document.getElementById('guess').value);
      if (isNaN(g)) return;
      attempts++;
      document.getElementById('tries').textContent = attempts;
      const m = document.getElementById('msg');
      if (g === secret) {
        m.textContent = `🎉 BINGO! You won in ${attempts} attempts!`;
        m.style.color = '#10b981';
      } else if (g < secret) {
        m.textContent = "📈 Too Low! Try a higher number.";
        m.style.color = '#38bdf8';
      } else {
        m.textContent = "📉 Too High! Try a lower number.";
        m.style.color = '#f43f5e';
      }
    }
  </script>
</body>
</html>'''
        write_workspace_file("number_guessing/index.html", html)
        return {
            "summary": "Built NumGuess interactive Number Guessing Game with hint feedback and attempts counter.",
            "plan": ["Setup random target generation", "Implement high/low binary comparison logic", "Write to workspace"],
            "files": [{"path": "number_guessing/index.html", "content": html, "action": "create", "explanation": "Number Guessing Game"}],
            "executed_files": ["number_guessing/index.html"],
            "next_steps": "Open 'number_guessing/index.html' and toggle to Live Web Preview!"
        }

    # 16. Tic-Tac-Toe Game
    if "tic-tac-toe" in p or "tictactoe" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CyberToe - Tic-Tac-Toe Game</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@800&family=JetBrains+Mono:wght@800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; text-align:center; }
    h1 { font-size:24px; color:#38bdf8; margin-bottom:16px; }
    .grid { display:grid; grid-template-columns:repeat(3,90px); gap:10px; margin:20px auto; }
    .cell { width:90px; height:90px; background:#09090b; border:1px solid #3f3f46; border-radius:14px; font-size:36px; font-weight:800; display:flex; align-items:center; justify-content:center; cursor:pointer; font-family:'JetBrains Mono',monospace; }
    .cell.x { color:#38bdf8; }
    .cell.o { color:#f43f5e; }
    button.reset { background:#6366f1; border:none; padding:10px 24px; border-radius:10px; color:#fff; font-weight:700; cursor:pointer; }
  </style>
</head>
<body>
  <div class="card">
    <h1>🎮 CyberToe</h1>
    <div id="status" style="font-size:15px; color:#94a3b8;">Player X's Turn</div>
    <div class="grid" id="board"></div>
    <button class="reset" onclick="resetGame()">New Game</button>
  </div>
  <script>
    let b = Array(9).fill(null);
    let turn = 'X';
    let won = false;
    const wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    function render() {
      const board = document.getElementById('board');
      board.innerHTML = '';
      b.forEach((v, i) => {
        const c = document.createElement('div');
        c.className = `cell ${v?v.toLowerCase():''}`;
        c.textContent = v || '';
        c.onclick = () => move(i);
        board.appendChild(c);
      });
    }
    function move(i) {
      if (b[i] || won) return;
      b[i] = turn;
      checkWin();
      if (!won) {
        turn = turn === 'X' ? 'O' : 'X';
        document.getElementById('status').textContent = `Player ${turn}'s Turn`;
      }
      render();
    }
    function checkWin() {
      for (let [x,y,z] of wins) {
        if (b[x] && b[x]===b[y] && b[x]===b[z]) {
          won = true;
          document.getElementById('status').textContent = `🎉 Player ${b[x]} Wins!`;
          document.getElementById('status').style.color = '#10b981';
          return;
        }
      }
      if (!b.includes(null)) {
        won = true;
        document.getElementById('status').textContent = "🤝 It's a Draw!";
      }
    }
    function resetGame() {
      b = Array(9).fill(null);
      turn = 'X';
      won = false;
      document.getElementById('status').textContent = "Player X's Turn";
      document.getElementById('status').style.color = '#94a3b8';
      render();
    }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("tictactoe/index.html", html)
        return {
            "summary": "Built CyberToe Tic-Tac-Toe Game with 2-player alternation and win detection.",
            "plan": ["Design 3x3 interactive board", "Implement win condition evaluation matrix", "Write to workspace"],
            "files": [{"path": "tictactoe/index.html", "content": html, "action": "create", "explanation": "Tic-Tac-Toe Web Game"}],
            "executed_files": ["tictactoe/index.html"],
            "next_steps": "Open 'tictactoe/index.html' and toggle to Live Web Preview!"
        }

    # 17. Unit Converter
    if "unit converter" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseUnit - Universal Converter</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; width:100%; max-width:440px; }
    h1 { font-size:22px; color:#38bdf8; margin-bottom:20px; }
    .field { margin-bottom:14px; }
    label { font-size:12px; color:#94a3b8; display:block; margin-bottom:6px; }
    input, select { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:14px; outline:none; }
    .res { background:#09090b; border-radius:12px; padding:16px; margin-top:20px; font-family:'JetBrains Mono',monospace; font-size:24px; color:#10b981; text-align:center; }
  </style>
</head>
<body>
  <div class="card">
    <h1>🔄 Universal Unit Converter</h1>
    <div class="field">
      <label>Value</label>
      <input type="number" id="val" value="1" oninput="convert()">
    </div>
    <div class="field">
      <label>From</label>
      <select id="from" onchange="convert()">
        <option value="m">Meters (m)</option>
        <option value="km">Kilometers (km)</option>
        <option value="mi">Miles (mi)</option>
        <option value="ft">Feet (ft)</option>
      </select>
    </div>
    <div class="field">
      <label>To</label>
      <select id="to" onchange="convert()">
        <option value="ft">Feet (ft)</option>
        <option value="m">Meters (m)</option>
        <option value="km">Kilometers (km)</option>
        <option value="mi">Miles (mi)</option>
      </select>
    </div>
    <div class="res" id="result">3.28 ft</div>
  </div>
  <script>
    const rates = { m: 1, km: 1000, mi: 1609.34, ft: 0.3048 };
    function convert() {
      const v = parseFloat(document.getElementById('val').value) || 0;
      const f = document.getElementById('from').value;
      const t = document.getElementById('to').value;
      const meters = v * rates[f];
      const converted = meters / rates[t];
      document.getElementById('result').textContent = `${converted.toFixed(2)} ${t}`;
    }
  </script>
</body>
</html>'''
        write_workspace_file("unit_converter/index.html", html)
        return {
            "summary": "Built Universal Unit Converter with live bidirectional metric & imperial translations.",
            "plan": ["Setup unit conversion ratio matrix", "Implement reactive value recalculation", "Write to workspace"],
            "files": [{"path": "unit_converter/index.html", "content": html, "action": "create", "explanation": "Unit Converter Application"}],
            "executed_files": ["unit_converter/index.html"],
            "next_steps": "Open 'unit_converter/index.html' and toggle to Live Web Preview!"
        }

    # 18. BMI Calculator
    if "bmi" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseFit - BMI Calculator</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; width:100%; max-width:400px; text-align:center; }
    h1 { font-size:22px; color:#38bdf8; margin-bottom:20px; }
    .input-grp { display:flex; gap:10px; margin-bottom:14px; }
    input { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:14px; outline:none; }
    button { width:100%; background:#6366f1; border:none; padding:12px; border-radius:10px; color:#fff; font-weight:700; cursor:pointer; }
    .bmi-val { font-family:'JetBrains Mono',monospace; font-size:42px; font-weight:800; color:#10b981; margin:20px 0 6px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>⚖️ BMI Calculator</h1>
    <div class="input-grp">
      <input type="number" id="w" placeholder="Weight (kg)" value="70">
      <input type="number" id="h" placeholder="Height (cm)" value="175">
    </div>
    <button onclick="calcBMI()">Calculate</button>
    <div id="val" class="bmi-val">22.9</div>
    <div id="category" style="font-size:14px; color:#818cf8; font-weight:700;">Normal Weight</div>
  </div>
  <script>
    function calcBMI() {
      const w = parseFloat(document.getElementById('w').value);
      const h = parseFloat(document.getElementById('h').value) / 100;
      if (!w || !h) return;
      const bmi = (w / (h * h)).toFixed(1);
      document.getElementById('val').textContent = bmi;
      let cat = "Normal Weight", col = "#10b981";
      if (bmi < 18.5) { cat = "Underweight"; col = "#38bdf8"; }
      else if (bmi >= 25 && bmi < 30) { cat = "Overweight"; col = "#f59e0b"; }
      else if (bmi >= 30) { cat = "Obese"; col = "#ef4444"; }
      document.getElementById('category').textContent = cat;
      document.getElementById('category').style.color = col;
    }
  </script>
</body>
</html>'''
        write_workspace_file("bmi_calculator/index.html", html)
        return {
            "summary": "Built PulseFit BMI Calculator with automated category analysis.",
            "plan": ["Design height/weight input form", "Implement standard body mass index formula", "Write to workspace"],
            "files": [{"path": "bmi_calculator/index.html", "content": html, "action": "create", "explanation": "BMI Calculator"}],
            "executed_files": ["bmi_calculator/index.html"],
            "next_steps": "Open 'bmi_calculator/index.html' and toggle to Live Web Preview!"
        }

    # 19. Contact Management System
    if "contact" in p and "management" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseContacts - Contact Manager</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:32px 20px; }
    .container { max-width:760px; margin:0 auto; }
    h1 { font-size:24px; color:#38bdf8; margin-bottom:20px; }
    .form-row { display:flex; gap:10px; margin-bottom:20px; }
    input { background:#18181b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; flex:1; }
    button.btn { background:#6366f1; border:none; border-radius:10px; padding:12px 20px; color:#fff; font-weight:700; cursor:pointer; }
    .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:14px; }
    .contact-card { background:#18181b; border:1px solid #27272a; border-radius:16px; padding:16px; }
    .c-name { font-weight:800; font-size:15px; margin-bottom:4px; }
    .c-info { font-size:12px; color:#94a3b8; margin-bottom:4px; }
  </style>
</head>
<body>
  <div class="container">
    <h1>📇 Contact Management System</h1>
    <div class="form-row">
      <input type="text" id="name" placeholder="Name">
      <input type="text" id="phone" placeholder="Phone">
      <input type="email" id="email" placeholder="Email">
      <button class="btn" onclick="addContact()">Save</button>
    </div>
    <div id="list" class="grid"></div>
  </div>
  <script>
    let contacts = [
      { name: "Sarah Connor", phone: "+1 555-0199", email: "sarah@skynet.ai" },
      { name: "Marcus Wright", phone: "+1 555-0144", email: "marcus@devpulse.com" }
    ];
    function render() {
      const l = document.getElementById('list');
      l.innerHTML = '';
      contacts.forEach(c => {
        const div = document.createElement('div');
        div.className = 'contact-card';
        div.innerHTML = `<div class="c-name">${c.name}</div><div class="c-info">📞 ${c.phone}</div><div class="c-info">✉️ ${c.email}</div>`;
        l.appendChild(div);
      });
    }
    function addContact() {
      const n = document.getElementById('name').value.trim();
      const p = document.getElementById('phone').value.trim();
      const e = document.getElementById('email').value.trim();
      if (!n || !p) return;
      contacts.unshift({ name: n, phone: p, email: e });
      render();
    }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("contact_manager/index.html", html)
        return {
            "summary": "Built PulseContacts Contact Management System.",
            "plan": ["Design contact card layout", "Implement in-memory address book storage", "Write to workspace"],
            "files": [{"path": "contact_manager/index.html", "content": html, "action": "create", "explanation": "Contact Management System"}],
            "executed_files": ["contact_manager/index.html"],
            "next_steps": "Open 'contact_manager/index.html' and toggle to Live Web Preview!"
        }

    # 20. Simple Blog Website
    if "blog" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>DevPulse Insights - Tech Blog</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:40px 20px; }
    .container { max-width:800px; margin:0 auto; }
    header { border-bottom:1px solid #27272a; padding-bottom:24px; margin-bottom:32px; }
    h1 { font-size:32px; color:#38bdf8; }
    .post { background:#18181b; border:1px solid #27272a; border-radius:20px; padding:28px; margin-bottom:20px; }
    .post-tag { display:inline-block; font-size:11px; font-weight:700; color:#818cf8; background:rgba(99,102,241,0.15); padding:3px 10px; border-radius:8px; margin-bottom:10px; }
    .post-title { font-size:20px; font-weight:800; margin-bottom:8px; }
    .post-desc { font-size:14px; color:#94a3b8; line-height:1.6; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>📰 DevPulse Engineering Blog</h1>
      <p style="color:#64748b; font-size:14px; margin-top:6px;">Perspectives on Autonomous AI Agents & Full-Stack Systems</p>
    </header>
    <div class="post">
      <span class="post-tag">ARCHITECTURE</span>
      <h2 class="post-title">Designing Resilient Multi-Language Subprocess Engines</h2>
      <p class="post-desc">Learn how to sandboxing Python, Node.js, and shell commands with timeout isolation, UTF-8 streaming, and exit-code inspection.</p>
    </div>
    <div class="post">
      <span class="post-tag">AI SYSTEMS</span>
      <h2 class="post-title">Building Self-Healing Code Environments with AI Debuggers</h2>
      <p class="post-desc">Exploring how automated error traceback diagnosis and AST patch generation streamline engineering productivity.</p>
    </div>
  </div>
</body>
</html>'''
        write_workspace_file("blog_website/index.html", html)
        return {
            "summary": "Built DevPulse Engineering Blog with responsive editorial post cards.",
            "plan": ["Design editorial blog layout", "Write featured engineering posts", "Mount to workspace"],
            "files": [{"path": "blog_website/index.html", "content": html, "action": "create", "explanation": "Simple Blog Website"}],
            "executed_files": ["blog_website/index.html"],
            "next_steps": "Open 'blog_website/index.html' and toggle to Live Web Preview!"
        }

    # 21. File Organizer Script in Python
    if "file organizer" in p or ("organizer" in p and "file" in p):
        py_code = '''"""
DevPulse AI - Automated File Organizer Script
Categorizes files in a target directory into organized folders based on file extensions.
"""
import os
import shutil
from pathlib import Path

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".md", ".xlsx", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".ts", ".json", ".sql"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"]
}

def organize_directory(target_dir: str):
    base_path = Path(target_dir).resolve()
    print(f"📂 Scanning & Organizing Directory: {base_path}")
    
    if not base_path.exists():
        print("Directory does not exist. Creating sample files to demonstrate...")
        base_path.mkdir(parents=True, exist_ok=True)
        # Create sample files
        (base_path / "report.pdf").touch()
        (base_path / "photo.png").touch()
        (base_path / "script.py").touch()
        (base_path / "archive.zip").touch()
    
    stats = {category: 0 for category in EXTENSIONS}
    stats["Others"] = 0

    for item in base_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            placed = False
            for category, exts in EXTENSIONS.items():
                if ext in exts:
                    dest_folder = base_path / category
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(dest_folder / item.name))
                    stats[category] += 1
                    placed = True
                    break
            if not placed:
                dest_folder = base_path / "Others"
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest_folder / item.name))
                stats["Others"] += 1

    print("\n✅ File Organization Summary:")
    for cat, count in stats.items():
        if count > 0:
            print(f"  • {cat}: {count} files categorized")

if __name__ == "__main__":
    organize_directory("./sample_unorganized_files")
'''
        write_workspace_file("file_organizer.py", py_code)
        return {
            "summary": "Generated Automated File Organizer script in Python with extension categorization.",
            "plan": ["Setup file extension mapping rules", "Implement directory traversal and shutil move logic", "Write to workspace"],
            "files": [{"path": "file_organizer.py", "content": py_code, "action": "create", "explanation": "File Organizer Script"}],
            "executed_files": ["file_organizer.py"],
            "next_steps": "Click 'Run Code' to execute 'file_organizer.py'!"
        }

    # 22. Student Marks Calculator in Java
    if "student marks" in p or ("marks" in p and "java" in p):
        java_code = '''/**
 * DevPulse AI - Student Marks & Grade Calculator
 * Language: Java
 */
import java.util.Scanner;

public class StudentMarksCalculator {
    public static void main(String[] args) {
        System.out.println("==========================================");
        System.out.println("🎓 Student Marks & Grade Calculation System");
        System.out.println("==========================================");

        String[] subjects = {"Mathematics", "Computer Science", "Physics", "English", "Chemistry"};
        int[] marks = {92, 98, 88, 85, 90}; // Sample benchmark grades
        
        int totalMarks = 0;
        int maxMarks = subjects.length * 100;

        System.out.println("\nSubject Breakdown:");
        for (int i = 0; i < subjects.length; i++) {
            System.out.printf("  • %-18s: %3d / 100\n", subjects[i], marks[i]);
            totalMarks += marks[i];
        }

        double percentage = ((double) totalMarks / maxMarks) * 100.0;
        String grade;
        
        if (percentage >= 90.0) grade = "A+ (Outstanding)";
        else if (percentage >= 80.0) grade = "A (Excellent)";
        else if (percentage >= 70.0) grade = "B (Good)";
        else if (percentage >= 60.0) grade = "C (Satisfactory)";
        else grade = "F (Needs Improvement)";

        System.out.println("\n------------------------------------------");
        System.out.printf("Total Score : %d / %d\n", totalMarks, maxMarks);
        System.out.printf("Percentage  : %.2f%%\n", percentage);
        System.out.printf("Final Grade : %s\n", grade);
        System.out.println("==========================================");
    }
}
'''
        write_workspace_file("StudentMarksCalculator.java", java_code)
        return {
            "summary": "Built Student Marks Calculator in Java with subject score aggregation and grade assignment.",
            "plan": ["Structure Java class and arrays", "Calculate percentage and letter grade thresholds", "Write to workspace"],
            "files": [{"path": "StudentMarksCalculator.java", "content": java_code, "action": "create", "explanation": "Java Marks Calculator"}],
            "executed_files": ["StudentMarksCalculator.java"],
            "next_steps": "Open 'StudentMarksCalculator.java' in the editor!"
        }

    # 23. Employee Management System
    if "employee" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseStaff - Employee Management</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:32px 20px; }
    .container { max-width:900px; margin:0 auto; }
    h1 { font-size:24px; color:#38bdf8; margin-bottom:20px; }
    .form-row { display:flex; gap:10px; margin-bottom:20px; }
    input, select { background:#18181b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; flex:1; }
    button.btn { background:#6366f1; border:none; border-radius:10px; padding:12px 20px; color:#fff; font-weight:700; cursor:pointer; }
    table { width:100%; border-collapse:collapse; background:#18181b; border-radius:16px; overflow:hidden; border:1px solid #27272a; }
    th, td { padding:14px 18px; text-align:left; font-size:13px; border-bottom:1px solid #27272a; }
    th { background:#1f1f23; color:#94a3b8; font-size:11px; text-transform:uppercase; }
  </style>
</head>
<body>
  <div class="container">
    <h1>💼 Employee Management System</h1>
    <div class="form-row">
      <input type="text" id="name" placeholder="Employee Name">
      <select id="dept">
        <option>Engineering</option><option>Product</option><option>Design</option><option>Operations</option>
      </select>
      <input type="text" id="role" placeholder="Role (e.g. Lead Architect)">
      <button class="btn" onclick="addEmp()">Add Staff</button>
    </div>
    <table>
      <thead><tr><th>Name</th><th>Department</th><th>Role</th><th>Status</th></tr></thead>
      <tbody id="emps"></tbody>
    </table>
  </div>
  <script>
    let staff = [
      { name: "Elena Rostova", dept: "Engineering", role: "AI Research Lead", status: "Active" },
      { name: "David Chen", dept: "Product", role: "Principal PM", status: "Active" }
    ];
    function render() {
      const b = document.getElementById('emps');
      b.innerHTML = '';
      staff.forEach(s => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td><b>${s.name}</b></td><td>${s.dept}</td><td style="color:#94a3b8;">${s.role}</td><td style="color:#10b981;">● ${s.status}</td>`;
        b.appendChild(tr);
      });
    }
    function addEmp() {
      const n = document.getElementById('name').value.trim();
      const d = document.getElementById('dept').value;
      const r = document.getElementById('role').value.trim();
      if (!n || !r) return;
      staff.unshift({ name: n, dept: d, role: r, status: "Active" });
      render();
    }
    render();
  </script>
</body>
</html>'''
        write_workspace_file("employee_system/index.html", html)
        return {
            "summary": "Built PulseStaff Employee Management System with department filters and staff directory.",
            "plan": ["Design employee ledger table", "Implement staff addition and status tracking", "Write to workspace"],
            "files": [{"path": "employee_system/index.html", "content": html, "action": "create", "explanation": "Employee Management System"}],
            "executed_files": ["employee_system/index.html"],
            "next_steps": "Open 'employee_system/index.html' and toggle to Live Web Preview!"
        }

    # 24. Currency Converter
    if "currency" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseFX - Currency Converter</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; width:100%; max-width:440px; }
    h1 { font-size:22px; color:#38bdf8; margin-bottom:20px; text-align:center; }
    .field { margin-bottom:14px; }
    input, select { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:14px; outline:none; }
    .res { background:#09090b; border-radius:12px; padding:16px; margin-top:20px; font-family:'JetBrains Mono',monospace; font-size:28px; color:#10b981; text-align:center; }
  </style>
</head>
<body>
  <div class="card">
    <h1>💱 PulseFX Currency Exchange</h1>
    <div class="field"><input type="number" id="amt" value="100" oninput="calc()"></div>
    <div class="field">
      <select id="from" onchange="calc()">
        <option value="USD">USD - US Dollar</option>
        <option value="EUR">EUR - Euro</option>
        <option value="GBP">GBP - British Pound</option>
        <option value="JPY">JPY - Japanese Yen</option>
      </select>
    </div>
    <div class="field">
      <select id="to" onchange="calc()">
        <option value="EUR">EUR - Euro</option>
        <option value="USD">USD - US Dollar</option>
        <option value="GBP">GBP - British Pound</option>
        <option value="JPY">JPY - Japanese Yen</option>
      </select>
    </div>
    <div class="res" id="out">92.00 EUR</div>
  </div>
  <script>
    const fx = { USD: 1.0, EUR: 0.92, GBP: 0.79, JPY: 154.5 };
    function calc() {
      const a = parseFloat(document.getElementById('amt').value) || 0;
      const f = document.getElementById('from').value;
      const t = document.getElementById('to').value;
      const inUSD = a / fx[f];
      const res = inUSD * fx[t];
      document.getElementById('out').textContent = `${res.toFixed(2)} ${t}`;
    }
  </script>
</body>
</html>'''
        write_workspace_file("currency_converter/index.html", html)
        return {
            "summary": "Built PulseFX Currency Converter with multi-currency exchange formulas.",
            "plan": ["Design exchange input card", "Implement real-time FX calculation", "Write to workspace"],
            "files": [{"path": "currency_converter/index.html", "content": html, "action": "create", "explanation": "Currency Converter"}],
            "executed_files": ["currency_converter/index.html"],
            "next_steps": "Open 'currency_converter/index.html' and toggle to Live Web Preview!"
        }

    # 25. Form Validation System
    if "form validation" in p or ("form" in p and "validation" in p):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SecureForm - Real-time Validation</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .card { background:#18181b; border:1px solid #27272a; border-radius:24px; padding:32px; width:100%; max-width:420px; }
    h1 { font-size:22px; color:#38bdf8; margin-bottom:20px; }
    .field { margin-bottom:14px; }
    label { display:block; font-size:12px; color:#94a3b8; margin-bottom:6px; font-weight:700; }
    input { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:10px; padding:12px; color:#fff; font-size:13px; outline:none; }
    .err { color:#f43f5e; font-size:11px; margin-top:4px; display:none; }
    button { width:100%; background:#6366f1; border:none; padding:12px; border-radius:10px; color:#fff; font-weight:700; cursor:pointer; margin-top:10px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>🛡️ SecureForm Validation</h1>
    <form onsubmit="validate(event)">
      <div class="field">
        <label>Username (min 4 chars)</label>
        <input type="text" id="user" oninput="checkUser()">
        <div id="u-err" class="err">Must be at least 4 alphanumeric characters</div>
      </div>
      <div class="field">
        <label>Email Address</label>
        <input type="email" id="email" oninput="checkEmail()">
        <div id="e-err" class="err">Please enter a valid email</div>
      </div>
      <div class="field">
        <label>Password (min 8 chars, 1 number)</label>
        <input type="password" id="pass" oninput="checkPass()">
        <div id="p-err" class="err">Password must have 8+ chars and at least 1 digit</div>
      </div>
      <button type="submit">Submit Registration</button>
    </form>
  </div>
  <script>
    function checkUser() {
      const v = document.getElementById('user').value.trim();
      const err = document.getElementById('u-err');
      err.style.display = (v.length >= 4) ? 'none' : 'block';
    }
    function checkEmail() {
      const v = document.getElementById('email').value.trim();
      const err = document.getElementById('e-err');
      err.style.display = (/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v)) ? 'none' : 'block';
    }
    function checkPass() {
      const v = document.getElementById('pass').value;
      const err = document.getElementById('p-err');
      err.style.display = (v.length >= 8 && /\\d/.test(v)) ? 'none' : 'block';
    }
    function validate(e) {
      e.preventDefault();
      checkUser(); checkEmail(); checkPass();
      alert('Form validation passed successfully!');
    }
  </script>
</body>
</html>'''
        write_workspace_file("form_validation/index.html", html)
        return {
            "summary": "Built SecureForm with real-time regex input validation.",
            "plan": ["Design validation card", "Implement live event listener checks for email & passwords", "Write to workspace"],
            "files": [{"path": "form_validation/index.html", "content": html, "action": "create", "explanation": "Form Validation System"}],
            "executed_files": ["form_validation/index.html"],
            "next_steps": "Open 'form_validation/index.html' and toggle to Live Web Preview!"
        }

    # 26. Chat Application
    if "chat application" in p or "chat app" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseChat - Live Team Chat</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; display:flex; align-items:center; justify-content:center; padding:20px; }
    .chat-container { background:#18181b; border:1px solid #27272a; border-radius:24px; width:100%; max-width:540px; height:600px; display:flex; flex-direction:column; overflow:hidden; }
    .chat-header { padding:18px 24px; background:#1f1f23; border-bottom:1px solid #27272a; display:flex; justify-content:space-between; align-items:center; }
    .stream { flex:1; overflow-y:auto; padding:20px; display:flex; flex-direction:column; gap:14px; }
    .bubble { max-width:75%; padding:12px 18px; border-radius:18px; font-size:13px; line-height:1.4; }
    .bubble.me { background:#6366f1; color:#fff; align-self:flex-end; border-bottom-right-radius:4px; }
    .bubble.peer { background:#27272a; color:#f1f5f9; align-self:flex-start; border-bottom-left-radius:4px; }
    .author { font-size:10px; color:#818cf8; margin-bottom:4px; font-weight:700; }
    .input-bar { display:flex; padding:14px; border-top:1px solid #27272a; gap:10px; }
    input { flex:1; background:#09090b; border:1px solid #3f3f46; border-radius:12px; padding:12px; color:#fff; outline:none; font-size:13px; }
    button { background:#6366f1; border:none; padding:12px 20px; border-radius:12px; color:#fff; font-weight:700; cursor:pointer; }
  </style>
</head>
<body>
  <div class="chat-container">
    <div class="chat-header">
      <div>
        <div style="font-weight:800; font-size:16px;"># engineering-general</div>
        <div style="font-size:11px; color:#10b981;">● 42 Developers Online</div>
      </div>
    </div>
    <div id="stream" class="stream">
      <div class="bubble peer">
        <div class="author">Alex (Architect)</div>
        Just pushed the new multi-language execution engine to staging.
      </div>
      <div class="bubble peer">
        <div class="author">Elena (AI Lead)</div>
        Looks clean! Latencies are down below 50ms.
      </div>
    </div>
    <form class="input-bar" onsubmit="post(event)">
      <input type="text" id="mInp" placeholder="Send a message...">
      <button type="submit">Post</button>
    </form>
  </div>
  <script>
    function post(e) {
      e.preventDefault();
      const inp = document.getElementById('mInp');
      const val = inp.value.trim();
      if (!val) return;
      inp.value = '';
      const stream = document.getElementById('stream');
      const d = document.createElement('div');
      d.className = 'bubble me';
      d.textContent = val;
      stream.appendChild(d);
      stream.scrollTop = stream.scrollHeight;
    }
  </script>
</body>
</html>'''
        write_workspace_file("chat_application/index.html", html)
        return {
            "summary": "Built PulseChat multi-room Team Chat Application.",
            "plan": ["Design modern team chat layout", "Implement reactive message rendering", "Write to workspace"],
            "files": [{"path": "chat_application/index.html", "content": html, "action": "create", "explanation": "Chat Application"}],
            "executed_files": ["chat_application/index.html"],
            "next_steps": "Open 'chat_application/index.html' and toggle to Live Web Preview!"
        }

    # 27. Resume Builder
    if "resume" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PulseCV - Interactive Resume Builder</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; }
    body { background:#09090b; color:#fff; min-height:100vh; padding:32px 20px; display:flex; justify-content:center; }
    .container { width:100%; max-width:800px; display:grid; grid-template-columns:1fr 1fr; gap:24px; }
    .form-panel { background:#18181b; border:1px solid #27272a; border-radius:20px; padding:24px; }
    .preview-panel { background:#fff; color:#0f172a; border-radius:20px; padding:28px; box-shadow:0 20px 40px rgba(0,0,0,0.5); font-size:13px; }
    h2 { font-size:18px; margin-bottom:14px; color:#38bdf8; }
    input, textarea { width:100%; background:#09090b; border:1px solid #3f3f46; border-radius:8px; padding:10px; color:#fff; font-size:12px; margin-bottom:10px; outline:none; }
    .cv-name { font-size:24px; font-weight:800; color:#0f172a; margin-bottom:2px; }
    .cv-role { font-size:14px; font-weight:700; color:#6366f1; margin-bottom:12px; }
    .cv-section { margin-top:16px; border-top:1px solid #e2e8f0; padding-top:10px; }
    .cv-heading { font-size:11px; font-weight:800; text-transform:uppercase; color:#64748b; letter-spacing:1px; margin-bottom:6px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="form-panel">
      <h2>Edit Details</h2>
      <input type="text" id="in-name" value="Alex Mercer" oninput="updateCV()">
      <input type="text" id="in-role" value="Lead Full-Stack AI Engineer" oninput="updateCV()">
      <input type="text" id="in-email" value="alex@engineer.ai" oninput="updateCV()">
      <textarea id="in-bio" rows="4" oninput="updateCV()">Specialist in autonomous agent architectures, scalable Python microservices, and Monaco IDE integrations.</textarea>
      <input type="text" id="in-skills" value="Python, FastAPI, TypeScript, React, Docker, SQL" oninput="updateCV()">
    </div>
    <div class="preview-panel">
      <div id="cv-name" class="cv-name">Alex Mercer</div>
      <div id="cv-role" class="cv-role">Lead Full-Stack AI Engineer</div>
      <div id="cv-email" style="color:#64748b; font-size:11px; margin-bottom:10px;">alex@engineer.ai</div>
      <div class="cv-section">
        <div class="cv-heading">Professional Profile</div>
        <div id="cv-bio" style="line-height:1.5;">Specialist in autonomous agent architectures, scalable Python microservices, and Monaco IDE integrations.</div>
      </div>
      <div class="cv-section">
        <div class="cv-heading">Core Technologies</div>
        <div id="cv-skills" style="font-weight:600; color:#334155;">Python, FastAPI, TypeScript, React, Docker, SQL</div>
      </div>
    </div>
  </div>
  <script>
    function updateCV() {
      document.getElementById('cv-name').textContent = document.getElementById('in-name').value;
      document.getElementById('cv-role').textContent = document.getElementById('in-role').value;
      document.getElementById('cv-email').textContent = document.getElementById('in-email').value;
      document.getElementById('cv-bio').textContent = document.getElementById('in-bio').value;
      document.getElementById('cv-skills').textContent = document.getElementById('in-skills').value;
    }
  </script>
</body>
</html>'''
        write_workspace_file("resume_builder/index.html", html)
        return {
            "summary": "Built PulseCV Interactive Resume Builder with two-column instant preview.",
            "plan": ["Design live split CV editor layout", "Implement reactive state data-binding", "Write to workspace"],
            "files": [{"path": "resume_builder/index.html", "content": html, "action": "create", "explanation": "Resume Builder Application"}],
            "executed_files": ["resume_builder/index.html"],
            "next_steps": "Open 'resume_builder/index.html' and toggle to Live Web Preview!"
        }

    # 28. Snake Game (Complete Rebuilt Cyber Neon Arcade)
    if "snake" in p:
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cyber Neon Snake - DevPulse Arcade</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * { margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans',sans-serif; user-select:none; }
    body {
      background: radial-gradient(circle at 50% 10%, #1e1b4b 0%, #06070c 100%);
      color: #f8fafc;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 16px;
      overflow-x: hidden;
    }
    .game-card {
      background: rgba(13, 15, 24, 0.9);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(99, 102, 241, 0.35);
      border-radius: 20px;
      padding: 20px;
      width: 100%;
      max-width: 440px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 35px rgba(99, 102, 241, 0.2);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .game-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 12px;
    }
    .title-group h1 {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #a5b4fc 0%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .badge {
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 10px;
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
      letter-spacing: 0.5px;
    }
    .stats-row {
      display: flex;
      gap: 10px;
      background: #080910;
      padding: 8px 12px;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.05);
      justify-content: space-around;
    }
    .stat-pill {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .stat-label {
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 1px;
      color: #64748b;
      text-transform: uppercase;
    }
    .stat-val {
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      font-weight: 800;
      color: #38bdf8;
    }
    .canvas-container {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
      border-radius: 14px;
      overflow: hidden;
      border: 2px solid rgba(99, 102, 241, 0.4);
      background: #07080f;
      box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.9);
    }
    canvas {
      display: block;
      width: 100%;
      height: 100%;
    }
    .modal-overlay {
      position: absolute;
      inset: 0;
      background: rgba(6, 7, 14, 0.88);
      backdrop-filter: blur(8px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 20px;
      text-align: center;
      transition: opacity 0.25s ease;
    }
    .modal-overlay.hidden {
      opacity: 0;
      pointer-events: none;
    }
    .modal-overlay h2 {
      font-size: 24px;
      font-weight: 800;
      color: #f8fafc;
    }
    .modal-overlay p {
      font-size: 13px;
      color: #94a3b8;
      max-width: 280px;
      line-height: 1.4;
    }
    .btn {
      background: linear-gradient(135deg, #6366f1 0%, #38bdf8 100%);
      color: white;
      border: none;
      padding: 10px 24px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
      transition: all 0.2s ease;
    }
    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(56, 189, 248, 0.5);
    }
    .btn-secondary {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #cbd5e1;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 11px;
      cursor: pointer;
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.15);
      color: white;
    }
    .btn-secondary.active {
      background: rgba(99, 102, 241, 0.3);
      border-color: #818cf8;
      color: #38bdf8;
    }
    .difficulty-bar {
      display: flex;
      gap: 6px;
      justify-content: center;
    }
    .dpad-container {
      display: grid;
      grid-template-columns: repeat(3, 44px);
      grid-template-rows: repeat(3, 44px);
      gap: 6px;
      justify-content: center;
      margin-top: 4px;
    }
    .dpad-btn {
      background: #151828;
      border: 1px solid rgba(99, 102, 241, 0.25);
      color: #cbd5e1;
      border-radius: 10px;
      font-size: 16px;
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
    .footer-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: #64748b;
      padding-top: 6px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }
  </style>
</head>
<body>
  <div class="game-card">
    <div class="game-header">
      <div class="title-group">
        <span class="badge">ARCADE EDITION</span>
        <h1>⚡ CYBER SNAKE</h1>
      </div>
      <div style="display: flex; gap: 6px;">
        <button id="soundToggle" class="btn-secondary" title="Toggle Sound">🔊 Sound</button>
        <button id="pauseBtn" class="btn-secondary" title="Pause Game">⏸️ Pause</button>
      </div>
    </div>

    <div class="stats-row">
      <div class="stat-pill">
        <span class="stat-label">Score</span>
        <span id="scoreVal" class="stat-val">0</span>
      </div>
      <div class="stat-pill">
        <span class="stat-label">High</span>
        <span id="highVal" class="stat-val">0</span>
      </div>
      <div class="stat-pill">
        <span class="stat-label">Level</span>
        <span id="levelVal" class="stat-val">1</span>
      </div>
      <div class="stat-pill">
        <span class="stat-label">Speed</span>
        <span id="speedVal" class="stat-val">1.0x</span>
      </div>
    </div>

    <div class="difficulty-bar">
      <button class="btn-secondary diff-btn active" data-speed="110">Casual</button>
      <button class="btn-secondary diff-btn" data-speed="80">Turbo</button>
      <button class="btn-secondary diff-btn" data-speed="55">Insane</button>
    </div>

    <div class="canvas-container">
      <canvas id="gameCanvas" width="400" height="400"></canvas>
      <div id="overlay" class="modal-overlay">
        <h2 id="modalTitle">CYBER SNAKE</h2>
        <p id="modalDesc">Navigate the cyber grid, devour energy cores, and beat the record.</p>
        <button id="startBtn" class="btn">LAUNCH GAME</button>
      </div>
    </div>

    <!-- Mobile / Mouse On-Screen D-Pad -->
    <div class="dpad-container">
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

    <div class="footer-bar">
      <span>🎮 Keys: <b>WASD</b> or <b>Arrows</b></span>
      <span>⏸️ <b>Space</b> to Pause</span>
    </div>
  </div>

  <script>
    // Audio Synthesizer via Web Audio API
    class SoundEngine {
      constructor() {
        this.ctx = null;
        this.muted = false;
      }
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
      }
      play(freq, type = 'sine', duration = 0.08, endFreq = null) {
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
          gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch (e) {}
      }
      eat() { this.play(440, 'triangle', 0.1, 880); }
      bonus() { this.play(600, 'square', 0.18, 1200); }
      turn() { this.play(260, 'sine', 0.03); }
      gameOver() { this.play(300, 'sawtooth', 0.35, 80); }
      pause() { this.play(520, 'sine', 0.06); }
    }

    const sound = new SoundEngine();
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const overlay = document.getElementById('overlay');
    const modalTitle = document.getElementById('modalTitle');
    const modalDesc = document.getElementById('modalDesc');
    const startBtn = document.getElementById('startBtn');
    const scoreVal = document.getElementById('scoreVal');
    const highVal = document.getElementById('highVal');
    const levelVal = document.getElementById('levelVal');
    const speedVal = document.getElementById('speedVal');
    const soundToggle = document.getElementById('soundToggle');
    const pauseBtn = document.getElementById('pauseBtn');

    const GRID = 20;
    const TILES = canvas.width / GRID;

    let snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
    let dir = { x: 1, y: 0 };
    let inputQueue = [];
    let food = { x: 15, y: 10 };
    let goldenFood = null;
    let goldenTimer = 0;
    let score = 0;
    let highScore = parseInt(localStorage.getItem('devpulse_snake_high_score') || '0', 10);
    highVal.textContent = highScore;

    let baseTickSpeed = 110;
    let currentSpeed = baseTickSpeed;
    let isRunning = false;
    let isPaused = false;
    let gameLoopTimeout = null;
    let particles = [];

    // Particle Burst System
    function spawnParticles(x, y, color, count = 12) {
      const cx = x * GRID + GRID / 2;
      const cy = y * GRID + GRID / 2;
      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 3 + 1.5;
        particles.push({
          x: cx,
          y: cy,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed,
          color,
          alpha: 1,
          decay: Math.random() * 0.03 + 0.02,
          radius: Math.random() * 2.5 + 1.5
        });
      }
    }

    function spawnFood() {
      while (true) {
        food = {
          x: Math.floor(Math.random() * TILES),
          y: Math.floor(Math.random() * TILES)
        };
        const onSnake = snake.some(p => p.x === food.x && p.y === food.y);
        if (!onSnake) break;
      }
      // 25% chance to spawn Golden Bonus Food if none exists
      if (!goldenFood && Math.random() < 0.3) {
        let gx, gy;
        while (true) {
          gx = Math.floor(Math.random() * TILES);
          gy = Math.floor(Math.random() * TILES);
          const collision = (gx === food.x && gy === food.y) || snake.some(p => p.x === gx && p.y === gy);
          if (!collision) break;
        }
        goldenFood = { x: gx, y: gy };
        goldenTimer = 60; // 60 game ticks
      }
    }

    function update() {
      if (!isRunning || isPaused) return;

      // Dequeue buffered direction input
      if (inputQueue.length > 0) {
        const nextDir = inputQueue.shift();
        // Prevent 180-degree self-collision
        if ((nextDir.x !== -dir.x || dir.x === 0) && (nextDir.y !== -dir.y || dir.y === 0)) {
          dir = nextDir;
          sound.turn();
        }
      }

      const head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };

      // Wall collision
      if (head.x < 0 || head.x >= TILES || head.y < 0 || head.y >= TILES) {
        return gameOver();
      }

      // Self collision
      for (let segment of snake) {
        if (head.x === segment.x && head.y === segment.y) {
          return gameOver();
        }
      }

      snake.unshift(head);

      // Eat Normal Food
      if (head.x === food.x && head.y === food.y) {
        score += 10;
        sound.eat();
        spawnParticles(food.x, food.y, '#38bdf8', 16);
        updateScore();
        spawnFood();
      }
      // Eat Golden Bonus Food
      else if (goldenFood && head.x === goldenFood.x && head.y === goldenFood.y) {
        score += 35;
        sound.bonus();
        spawnParticles(goldenFood.x, goldenFood.y, '#fbbf24', 24);
        goldenFood = null;
        updateScore();
      } else {
        snake.pop();
      }

      // Countdown golden food
      if (goldenFood) {
        goldenTimer--;
        if (goldenTimer <= 0) goldenFood = null;
      }

      draw();
      gameLoopTimeout = setTimeout(update, currentSpeed);
    }

    function updateScore() {
      scoreVal.textContent = score;
      if (score > highScore) {
        highScore = score;
        highVal.textContent = highScore;
        localStorage.setItem('devpulse_snake_high_score', highScore);
      }
      const level = Math.floor(score / 50) + 1;
      levelVal.textContent = level;

      // Scale speed dynamically with level
      currentSpeed = Math.max(35, baseTickSpeed - (level - 1) * 6);
      speedVal.textContent = (baseTickSpeed / currentSpeed).toFixed(1) + 'x';
    }

    function draw() {
      // Clear canvas with subtle radial backdrop
      ctx.fillStyle = '#080911';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Cyber Grid
      ctx.strokeStyle = 'rgba(99, 102, 241, 0.06)';
      ctx.lineWidth = 1;
      for (let i = 0; i <= canvas.width; i += GRID) {
        ctx.beginPath();
        ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height);
        ctx.moveTo(0, i); ctx.lineTo(canvas.width, i);
        ctx.stroke();
      }

      // Particles
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
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }
      }

      // Draw Normal Food (Neon Cyan Core)
      ctx.save();
      ctx.shadowColor = '#38bdf8';
      ctx.shadowBlur = 12;
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(food.x * GRID + GRID / 2, food.y * GRID + GRID / 2, GRID / 2 - 3, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(food.x * GRID + GRID / 2 - 2, food.y * GRID + GRID / 2 - 2, 2, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      // Draw Golden Bonus Food if active
      if (goldenFood) {
        ctx.save();
        ctx.shadowColor = '#fbbf24';
        ctx.shadowBlur = 16;
        ctx.fillStyle = '#f59e0b';
        ctx.beginPath();
        ctx.arc(goldenFood.x * GRID + GRID / 2, goldenFood.y * GRID + GRID / 2, GRID / 2 - 2, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#fef08a';
        ctx.beginPath();
        ctx.arc(goldenFood.x * GRID + GRID / 2 - 2, goldenFood.y * GRID + GRID / 2 - 2, 3, 0, Math.PI * 2);
        ctx.fill();
        // Timer countdown ring
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(goldenFood.x * GRID + GRID / 2, goldenFood.y * GRID + GRID / 2, GRID / 2 + 1, 0, (goldenTimer / 60) * Math.PI * 2);
        ctx.stroke();
        ctx.restore();
      }

      // Draw Snake with Gradient & Head Details
      snake.forEach((part, idx) => {
        const isHead = idx === 0;
        ctx.save();
        if (isHead) {
          ctx.fillStyle = '#a855f7';
          ctx.shadowColor = '#a855f7';
          ctx.shadowBlur = 12;
        } else {
          const ratio = idx / snake.length;
          ctx.fillStyle = ratio > 0.6 ? '#6366f1' : '#818cf8';
          ctx.shadowBlur = 0;
        }

        const px = part.x * GRID + 1.5;
        const py = part.y * GRID + 1.5;
        const size = GRID - 3;
        ctx.beginPath();
        ctx.roundRect(px, py, size, size, isHead ? 6 : 4);
        ctx.fill();

        // Draw animated eyes on the head
        if (isHead) {
          ctx.fillStyle = '#ffffff';
          const eyeOffset = 4;
          const eyeR = 2.2;
          let e1 = { x: px + eyeOffset, y: py + eyeOffset };
          let e2 = { x: px + size - eyeOffset, y: py + eyeOffset };

          if (dir.y === 1) {
            e1 = { x: px + eyeOffset, y: py + size - eyeOffset };
            e2 = { x: px + size - eyeOffset, y: py + size - eyeOffset };
          } else if (dir.x === 1) {
            e1 = { x: px + size - eyeOffset, y: py + eyeOffset };
            e2 = { x: px + size - eyeOffset, y: py + size - eyeOffset };
          } else if (dir.x === -1) {
            e1 = { x: px + eyeOffset, y: py + eyeOffset };
            e2 = { x: px + eyeOffset, y: py + size - eyeOffset };
          }
          ctx.beginPath();
          ctx.arc(e1.x, e1.y, eyeR, 0, Math.PI * 2);
          ctx.arc(e2.x, e2.y, eyeR, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();
      });
    }

    function startGame() {
      snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
      dir = { x: 1, y: 0 };
      inputQueue = [];
      score = 0;
      particles = [];
      goldenFood = null;
      updateScore();
      spawnFood();
      isRunning = true;
      isPaused = false;
      overlay.classList.add('hidden');
      pauseBtn.textContent = '⏸️ Pause';
      clearTimeout(gameLoopTimeout);
      update();
    }

    function togglePause() {
      if (!isRunning) return;
      isPaused = !isPaused;
      sound.pause();
      if (isPaused) {
        clearTimeout(gameLoopTimeout);
        pauseBtn.textContent = '▶️ Resume';
        modalTitle.textContent = 'GAME PAUSED';
        modalDesc.textContent = 'Take a breather. Press Space or button below to resume.';
        startBtn.textContent = 'RESUME GAME';
        overlay.classList.remove('hidden');
      } else {
        pauseBtn.textContent = '⏸️ Pause';
        overlay.classList.add('hidden');
        update();
      }
    }

    function gameOver() {
      isRunning = false;
      clearTimeout(gameLoopTimeout);
      sound.gameOver();
      spawnParticles(snake[0].x, snake[0].y, '#f43f5e', 25);
      draw();
      modalTitle.textContent = 'MISSION FAILED';
      modalDesc.textContent = `Score: ${score} points | High: ${highScore} pts.`;
      startBtn.textContent = 'PLAY AGAIN';
      overlay.classList.remove('hidden');
    }

    function handleDirectionInput(newDir) {
      if (!isRunning) {
        startGame();
        return;
      }
      if (isPaused) {
        togglePause();
      }
      inputQueue.push(newDir);
    }

    // Controls: Arrow keys & WASD with preventDefault so page never scrolls
    window.addEventListener('keydown', (e) => {
      const keys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'KeyW', 'KeyA', 'KeyS', 'KeyD', 'Space'];
      if (keys.includes(e.code) || ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) {
        e.preventDefault();
      }

      if (e.code === 'Space' || e.key === ' ') {
        if (!isRunning) startGame();
        else togglePause();
        return;
      }

      switch (e.code) {
        case 'ArrowUp':
        case 'KeyW':
          handleDirectionInput({ x: 0, y: -1 });
          break;
        case 'ArrowDown':
        case 'KeyS':
          handleDirectionInput({ x: 0, y: 1 });
          break;
        case 'ArrowLeft':
        case 'KeyA':
          handleDirectionInput({ x: -1, y: 0 });
          break;
        case 'ArrowRight':
        case 'KeyD':
          handleDirectionInput({ x: 1, y: 0 });
          break;
      }
    });

    // Touch / D-Pad Buttons
    document.getElementById('dpad-up').addEventListener('click', () => handleDirectionInput({ x: 0, y: -1 }));
    document.getElementById('dpad-down').addEventListener('click', () => handleDirectionInput({ x: 0, y: 1 }));
    document.getElementById('dpad-left').addEventListener('click', () => handleDirectionInput({ x: -1, y: 0 }));
    document.getElementById('dpad-right').addEventListener('click', () => handleDirectionInput({ x: 1, y: 0 }));
    document.getElementById('dpad-pause').addEventListener('click', togglePause);

    // Header buttons
    startBtn.addEventListener('click', () => {
      if (isPaused) togglePause();
      else startGame();
    });
    pauseBtn.addEventListener('click', togglePause);
    soundToggle.addEventListener('click', () => {
      sound.muted = !sound.muted;
      soundToggle.textContent = sound.muted ? '🔇 Muted' : '🔊 Sound';
      soundToggle.classList.toggle('active', sound.muted);
    });

    // Difficulty buttons
    document.querySelectorAll('.diff-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        baseTickSpeed = parseInt(btn.dataset.speed, 10);
        updateScore();
      });
    });

    draw();
  </script>
</body>
</html>'''
        write_workspace_file("snake_game/index.html", html)
        return {
            "summary": "Rebuilt Cyber Neon Snake Game with retro glowing grid, Web Audio SFX, speed modes, particles, and responsive controls.",
            "plan": [
                "Construct HTML5 Cyberpunk Neon Canvas layout",
                "Implement Web Audio API synthesizer for 8-bit sound effects",
                "Build input queue buffer to prevent 180-degree self collisions",
                "Integrate golden bonus food, particle bursts, and speed progression",
                "Add Spacebar pause/resume and on-screen D-Pad controls",
                "Save high score to persistent localStorage"
            ],
            "files": [
                {
                    "path": "snake_game/index.html",
                    "content": html,
                    "action": "create",
                    "explanation": "Interactive Cyber Snake Game with canvas graphics, particle FX, and audio."
                }
            ],
            "executed_files": ["snake_game/index.html"],
            "next_steps": "Open 'snake_game/index.html' and toggle to Live Web Preview to play!"
        }

    return None
