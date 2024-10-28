#!/bin/bash

# Set up a virtual environment in the 'venv' directory
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and install FastAPI and Uvicorn
pip install --upgrade pip
pip install fastapi uvicorn

# Run the FastAPI app (main.py) on host 0.0.0.0 and port 8000
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
