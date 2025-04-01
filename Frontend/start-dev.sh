#!/bin/bash

# Absolute path to backend
BACKEND_DIR="/workspaces/Hospital_Management-_System/backend"

# Activate virtual environment
source "$BACKEND_DIR/.venv/bin/activate"

# Install dependencies (optional but safe)
pip install -r "$BACKEND_DIR/requirements.txt"

# Start FastAPI backend
cd "$BACKEND_DIR"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
