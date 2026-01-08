#!/usr/bin/env python3

"""
Simple Task Manager Web Application
A real-life example of Flask web application for managing daily tasks
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for tasks (in real apps, use a database)
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False, "created": "2026-01-07"},
    {"id": 2, "title": "Complete Python assignment", "completed": False, "created": "2026-01-07"},
    {"id": 3, "title": "Read a book", "completed": True, "created": "2026-01-07"}
]

task_id_counter = 4

@app.route("/")
def index():
    """Home page showing all tasks"""
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t["completed"]])
    pending_tasks = total_tasks - completed_tasks
    
    return render_template("index.html", 
                         tasks=tasks, 
                         total=total_tasks,
                         completed=completed_tasks,
                         pending=pending_tasks)

@app.route("/add", methods=["POST"])
def add_task():
    """Add a new task"""
    global task_id_counter
    
    title = request.form.get("title")
    if title and title.strip():
        new_task = {
            "id": task_id_counter,
            "title": title.strip(),
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d")
        }
        tasks.append(new_task)
        task_id_counter += 1
    
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    """Mark a task as completed"""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    
    return redirect(url_for("index"))

@app.route("/about")
def about():
    """About page with application information"""
    return render_template("about.html")

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Task Manager Application Starting...")
    print("=" * 50)
    print("📝 Access the application at: http://localhost:5000")
    print("📊 Features: Add, Complete, and Delete Tasks")
    print("=" * 50)
    
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
