#!/bin/bash
# Build script for VAM Python application

set -e

echo "Building VAM Python Application..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Build completed successfully!"
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To run the app, execute: python main.py"
