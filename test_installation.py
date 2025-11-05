#!/usr/bin/env python3
"""
Test script to verify YouTube Transcript Downloader installation
Run this script to check if all dependencies are properly installed.
"""

import sys
import importlib
from pathlib import Path

def test_import(module_name, package_name=None):
    """Test if a module can be imported"""
    try:
        if package_name:
            importlib.import_module(module_name, package_name)
        else:
            importlib.import_module(module_name)
        print(f"✓ {module_name} is installed")
        return True
    except ImportError as e:
        print(f"✗ {module_name} is NOT installed - {e}")
        return False

def main():
    """Run installation tests"""
    print("YouTube Transcript Downloader - Installation Test")
    print("=" * 50)
    print("\nTesting Python version...")
    
    # Check Python version
    if sys.version_info >= (3, 7):
        print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} (requires 3.7+)")
    else:
        print(f"✗ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} (requires 3.7+)")
        sys.exit(1)
    
    print("\nTesting required packages...")
    
    # Test required packages
    required_packages = [
        ('pandas', None),
        ('youtube_transcript_api', None),
        ('yt_dlp', None),
        ('webvtt', None),
        ('tqdm', None),
    ]
    
    all_installed = True
    for module, package in required_packages:
        if not test_import(module, package):
            all_installed = False
    
    print("\nTesting project files...")
    
    # Test project files
    project_files = [
        'get_channel_transcripts.py',
        'clean_transcripts.py',
        'youtubecheck.py',
        'config.py',
        'README.md',
        'requirements.txt',
    ]
    
    for file in project_files:
        if Path(file).exists():
            print(f"✓ {file} found")
        else:
            print(f"✗ {file} NOT found")
            all_installed = False
    
    print("\n" + "=" * 50)
    if all_installed:
        print("✓ All tests passed! The YouTube Transcript Downloader is ready to use.")
        print("\nTry running:")
        print("  python get_channel_transcripts.py --csv example_videos.csv")
    else:
        print("✗ Some components are missing. Please run:")
        print("  pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()