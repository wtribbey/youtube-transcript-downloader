@echo off
REM YouTube Transcript Downloader - Setup Script for Windows
REM This script sets up the project environment

echo YouTube Transcript Downloader - Setup
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org
    pause
    exit /b 1
)

echo Python is installed
python --version
echo.
echo Creating virtual environment...

REM Create virtual environment
python -m venv .venv

REM Activate virtual environment
call .venv\Scripts\activate.bat

echo Virtual environment created
echo.
echo Installing dependencies...

REM Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Dependencies installed
echo.
echo Running installation test...
echo.

REM Run test
python test_installation.py

echo.
echo Setup complete!
echo.
echo To activate the virtual environment in the future, run:
echo   .venv\Scripts\activate.bat
echo.
echo To get started, try:
echo   python get_channel_transcripts.py --csv example_videos.csv
echo.
pause