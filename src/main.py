from typing import Annotated
from datetime import datetime, date
from pathlib import Path
import platform
import typer
import json

app = typer.Typer()

def get_tasks_dir() -> Path:
    if platform.system() == "Windows":
        base = Path.home() / "Documents"
    else:
        base = Path.home()

    tasks_dir = base / ".todo"
    tasks_dir.mkdir(exist_ok=True)
    return tasks_dir


TASKS_FILE = get_tasks_dir() / "tasks.json"
DONE_TASKS_FILE = get_tasks_dir() / "done_tasks.json"


def load_tasks() -> list:
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def load_done_tasks() -> list:
    if not DONE_TASKS_FILE.exists():
        return []
    with open(DONE_TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks: list):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def save_done_tasks(tasks: list):
    with open(DONE_TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

@app.command()
def add(
    task_name: Annotated[str, typer.Option(prompt="Enter the name of your task")],
    notes: Annotated[str, typer.Option(prompt="Enter any notes for the task")],
    date_due: Annotated[
        datetime, typer.Option(prompt="Enter the task due date (yyyy-mm-dd)")
    ],
):
    tasks = load_tasks()
    tasks.append(
        {
            "task_name": task_name,
            "notes": notes,
            "date_due": str(date_due.date()),
            "date_created": str(date.today()),
        }
    )
    save_tasks(tasks)
    typer.echo(f"Task '{task_name}' added.")


@app.command()
def rm():

    tasks = load_tasks()

    if not tasks:
        typer.echo("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        typer.echo(f"{i}. {t['task_name']} (due: {t['date_due']}) - {t['notes']}")

    index = typer.prompt("Which task would you like to delete? (Warning: permanent)")

    try:
        index = int(index)
        if not 1 <= index <= len(tasks):
            raise ValueError

    except ValueError:
        typer.echo(f"Invalid selection. Enter a number between 1 and {len(tasks)}")
        raise typer.Exit()

    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    typer.echo(f"Deleted: '{removed['task_name']}'")


@app.command()
def done():
    tasks = load_tasks()
    done_tasks = load_done_tasks()
    if not tasks:
        typer.echo("No tasks found.")
        return

    for i, t in enumerate(tasks, 1):
        typer.echo(f"{i}. {t['task_name']} (due: {t['date_due']}) - {t['notes']}")

    index = typer.prompt("Which task would you like to mark as done?")

    try:
        index = int(index)
        if not 1 <= index <= len(tasks):
            raise ValueError
    except ValueError:
        typer.echo(f"Invalid selection. Enter a number between 1 and {len(tasks)}")
        raise typer.Exit()

    completed = tasks.pop(index - 1)
    completed["date_completed"] = str(date.today())  # optional, but useful
    done_tasks.append(completed)  # append just the one task
    save_done_tasks(done_tasks)   # save updated done list
    save_tasks(tasks)             # save updated active list
    typer.echo(f"'{completed['task_name']}' marked as done.")


@app.command()
def ls():

    tasks = load_tasks()

    if not tasks:
        typer.echo("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        typer.echo(f"{i}. {t['task_name']} (due: {t['date_due']}) - {t['notes']}")


if __name__ == "__main__":
    app()
