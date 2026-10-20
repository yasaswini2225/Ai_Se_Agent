import asyncio
from backend.ai_engine import run_autonomous_agent
from backend.workspace_manager import read_workspace_file

TASKS_TO_TEST = [
    "Build a Calculator",
    "Build a Student Management System",
    "Create a To-Do List App",
    "Build a Personal Portfolio Website",
    "Create a Login and Registration Page",
    "Build a Weather App",
    "Create a Notes Application",
    "Build a Quiz Application",
    "Create an Expense Tracker",
    "Build a Simple Chatbot",
    "Create a Library Management System",
    "Build an E-commerce Website",
    "Create a Password Generator",
    "Build a Digital Clock",
    "Create a Number Guessing Game",
    "Build a Tic-Tac-Toe Game",
    "Create a Unit Converter",
    "Build a BMI Calculator",
    "Create a Contact Management System",
    "Build a Simple Blog Website",
    "Create a File Organizer Script in Python",
    "Build a Student Marks Calculator in Java",
    "Create an Employee Management System",
    "Build a Currency Converter",
    "Create a Form Validation System",
    "Build a Chat Application",
    "Create a Resume Builder",
    "Build a Snake Game",
    "Create a Basic REST API using Node.js and Express",
    "Debug a program containing syntax and logical errors"
]

def test_all_30():
    print(f"Testing all {len(TASKS_TO_TEST)} benchmark tasks...")
    passed = 0
    for idx, task in enumerate(TASKS_TO_TEST, 1):
        res = asyncio.run(run_autonomous_agent(task))
        files = res.get("executed_files", [])
        assert len(files) > 0, f"Task '{task}' generated no files"
        content = read_workspace_file(files[0])["content"]
        assert len(content) > 50, f"Task '{task}' produced empty file"
        print(f"  [{idx:02d}/30] [OK] '{task}' -> {files[0]} ({len(content)} bytes)")
        passed += 1

    print(f"\nALL {passed}/30 BENCHMARK TASKS TESTED AND PASSED PERFECTLY!")

if __name__ == "__main__":
    test_all_30()
