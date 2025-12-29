#!/bin/bash

# Setup script for audio-stretcher

echo "Setting up audio-stretcher..."

# Check for rubberband
if ! command -v rubberband &> /dev/null; then
    echo "⚠️  rubberband not found!"
    echo "Please install it:"
    echo "  sudo apt-get install rubberband-cli"
else
    echo "✅ rubberband found: $(which rubberband)"
fi

# Create venv if not exists
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✅ Virtual environment created at .venv"
fi

# Install
source .venv/bin/activate
pip install -e .
echo "✅ Installed audio-stretcher in editable mode"
