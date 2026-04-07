Write-Host "Installing todo..."

# Install uv if not present
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "Installing uv..."
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
}

# Install todo
uv tool install git+https://github.com/yourusername/todo.git

Write-Host "Done! Run 'todo' to get started."