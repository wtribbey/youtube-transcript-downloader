#!/bin/bash

# Git Setup and Push Script for YouTube Transcript Downloader
# This script initializes git and pushes to your GitHub repository

echo "==================================="
echo "GitHub Repository Setup"
echo "==================================="
echo ""

# Navigate to project directory
cd /Users/willt/PycharmProjects/youtubeurls

# Initialize git if not already done
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    echo "✓ Git initialized"
else
    echo "✓ Git already initialized"
fi

echo ""
echo "Adding all files to git..."
git add .

echo ""
echo "Creating initial commit..."
git commit -m "Initial commit: YouTube Transcript Downloader

- Bulk download YouTube transcripts from CSV input
- Smart duplicate removal in transcripts
- Dual extraction methods (API + yt-dlp fallback)
- Rate limiting and error handling
- Cookie support for restricted content
- Progress tracking with detailed logging"

echo ""
echo "✓ Files committed"
echo ""
echo "==================================="
echo "Now you need to:"
echo "==================================="
echo ""
echo "1. Go to https://github.com/new"
echo "2. Create a new repository named: youtube-transcript-downloader"
echo "3. DON'T initialize with README, .gitignore, or license"
echo "4. After creating, copy the repository URL"
echo ""
echo "5. Then run these commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/youtube-transcript-downloader.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "Replace YOUR_USERNAME with your actual GitHub username"
echo ""
echo "==================================="
echo ""
read -p "Press Enter when you've created the GitHub repository..."

echo ""
echo "What's your GitHub username? "
read github_username

if [ ! -z "$github_username" ]; then
    echo ""
    echo "Setting up remote repository..."
    git remote add origin https://github.com/${github_username}/youtube-transcript-downloader.git
    
    echo "Setting main branch..."
    git branch -M main
    
    echo ""
    echo "Pushing to GitHub..."
    echo "(You may be prompted for your GitHub credentials)"
    echo ""
    git push -u origin main
    
    echo ""
    echo "==================================="
    echo "✓ Repository pushed successfully!"
    echo "==================================="
    echo ""
    echo "Your repository is now available at:"
    echo "https://github.com/${github_username}/youtube-transcript-downloader"
    echo ""
else
    echo "No username provided. Please run the git remote commands manually."
fi