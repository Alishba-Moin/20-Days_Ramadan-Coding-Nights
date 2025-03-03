import click
import json
import os

# File to store tasks
Todo_file = "todo.json"

# Function to load tasks from the file
def todo_tasks():
    if not os.path.exists(Todo_file):
        return []  # Return empty list if file doesn't exist
    with open(Todo_file, "r") as file:
        return json.load(file)  # Load tasks from JSON file

# Function to save tasks to the file
def save_todo_tasks(tasks):
    with open(Todo_file, "w") as file:
        json.dump(tasks, file, indent=4)  # Save tasks in JSON format
    
@click.group()
def cli():
    '''Todo List Manager'''
    pass  # Group command to organize subcommands

# Command to add a new task
@click.command()
@click.argument("task")
@click.option("--category", default="General", help="Category of the task")
def add(task, category):
    '''Add new task in a list with a category'''
    tasks = todo_tasks()
    tasks.append({"task": task, "done": False, "category": category})  # Add task with default 'done' status
    save_todo_tasks(tasks)
    click.echo(f"Task Added Successfully: {task} (Category: {category})")

# Command to list all tasks
@click.command()
def list():
    '''List all tasks'''
    tasks = todo_tasks()
    if not tasks:
        click.echo("No Task Found!")  # Message if no tasks exist
        return
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"  # Mark completed tasks
        click.echo(f"{index}. {task['task']} [{status}]")

# Command to mark a task as completed
@click.command()
@click.argument("task_num", type=int)
def complete(task_num):
    """Mark a task as completed"""
    tasks = todo_tasks()
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True  # Update task status
        save_todo_tasks(tasks)
        click.echo(f"Task {task_num} marked as completed!")
    else:
        click.echo("Invalid task number.")

# Command to delete a task
@click.command()
@click.argument("task_num", type=int)
def delete(task_num):
    """Remove a task from the list"""
    tasks = todo_tasks()
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)  # Remove task by index
        save_todo_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']} from the list")
    else:
        click.echo("Invalid task number.")

# Command to search tasks by keyword
@click.command()
@click.argument("keyword")
def search(keyword):
    """Search for tasks by keyword"""
    tasks = todo_tasks()
    found_tasks = [task for task in tasks if keyword.lower() in task["task"].lower()]
    if not found_tasks:
        click.echo(f"No tasks found matching {keyword}.")
    else:
        click.echo(f"Tasks matching '{keyword}':")
        for index, task in enumerate(found_tasks, 1):
            status = "✓" if task["done"] else "✗"
            click.echo(f"{index}. {task['task']} [{status}] (Category: {task['category']})")

# Command to show task statistics
@click.command()
def stats():
    '''Show Task Statistics'''
    tasks = todo_tasks()
    total = len(tasks)
    completed = sum(1 for task in tasks if task['done'])  # Count completed tasks
    pending = total - completed  # Calculate pending tasks
    click.echo(f"📌Total Tasks: {total}")
    click.echo(f"✅ Completed Tasks: {completed}")
    click.echo(f"⏳ Pending Tasks: {pending}")

# Add commands to CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)
cli.add_command(search)
cli.add_command(stats)

# Entry point of the script
if __name__ == "__main__":
    cli()