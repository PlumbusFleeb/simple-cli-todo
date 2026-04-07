# simple-cli-todo

A lightweight command line task manager.

## Install

**Linux/macOS:**
```bash
curl -LsSf https://raw.githubusercontent.com/PlumbusFleeb/simple-cli-todo/main/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/PlumbusFleeb/simple-cli-todo/main/install.ps1 | iex
```
> **Note:** On Windows, if the `todo` command is not found after install, close and reopen PowerShell (or Terminal) and run the command again.

## Usage

### Add a task
```bash
todo add
```
You will be prompted for a task name, notes, and due date.

### List tasks
```bash
todo ls
```
Displays all pending tasks with their due dates and notes.

### Mark a task as done
```bash
todo done
```
Displays your task list and prompts you to select a task to mark as complete. Completed tasks are saved separately and removed from your active list.

### Remove a task
```bash
todo rm
```
Displays your task list and prompts you to select a task to permanently delete.

## Data

Tasks are stored locally as JSON files:
- **Linux/macOS:** `~/.todo/`
- **Windows:** `~/Documents/.todo/`

## Roadmap

### Sorting flag for `ls`
Add an optional flag to `todo ls` to sort tasks by different criteria:
```bash
todo ls --sort due      # sort by due date
todo ls --sort created  # sort by date created
todo ls --sort name     # sort alphabetically
```

### `stats` command
A new command to display insights about your tasks over time:
```bash
todo stats
```
Planned metrics:
- Total tasks completed
- Tasks completed within a given time period (e.g. last 7 or 30 days)
- Average time between task creation and completion
- Number of overdue tasks
- Most productive day/week based on completions