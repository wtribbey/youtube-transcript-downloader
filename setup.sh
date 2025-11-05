#!/bin/bash

# YouTube Transcript Downloader - Setup Script
# This script sets up the project environment

echo "YouTube Transcript Downloader - Setup"
echo "====================================="
echo ""

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    echo "✓ Python 3 is installed"
    python3 --version
else
    echo "✗ Python 3 is not installed"
    echo "Please install Python 3.7 or higher from https://www.python.org"
    exit 1
fi

echo ""
echo "Creating virtual environment..."

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    source .venv/Scripts/activate
else
    # macOS/Linux
    source .venv/bin/activate
fi

echo "✓ Virtual environment created"
echo ""
echo "Installing dependencies..."

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✓ Dependencies installed"
echo ""
echo "Running installation test..."
echo ""

# Run test
python3 test_installation.py

echo ""
echo "Setup complete!"
echo ""
echo "To activate the virtual environment in the future, run:"
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "  .venv\\Scripts\\activate"
else
    echo "  source .venv/bin/activate"
fi
echo ""
echo "To get started, try:"
echo "  python get_channel_transcripts.py --csv example_videos.csv"