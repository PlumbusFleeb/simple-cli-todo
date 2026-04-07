#!/bin/bash
set -e

echo "Installing todo..."

# Install uv if not present
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env
fi

# Install todo
uv tool install git+https://github.com/yourusername/todo.git

echo "Done! Run 'todo' to get started."