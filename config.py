"""
Configuration settings for YouTube Transcript Downloader
"""

# Default settings
DEFAULT_OUTPUT_DIR = "transcripts"
DEFAULT_RATE_LIMIT = 0.4  # seconds between requests
DEFAULT_GLOB_PATTERN = "*.txt"

# Language preferences for transcripts
TRANSCRIPT_LANGUAGES = ['en', 'en-US', 'en-GB']

# File naming
MAX_FILENAME_LENGTH = 120
DEFAULT_FILE_PREFIX_DIGITS = 4

# Video URL patterns
YOUTUBE_DOMAINS = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']

# User agent for yt-dlp
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# CSV column names to look for (case-insensitive)
URL_COLUMN_NAMES = ['url', 'link', 'video', 'video_url']
TITLE_COLUMN_NAMES = ['title', 'name', 'video_title']
DATE_COLUMN_NAMES = ['date', 'upload_date', 'published']

# Output file headers
TRANSCRIPT_HEADER_SEPARATOR = "-" * 80

# Error handling
MAX_RETRY_ATTEMPTS = 3
ERROR_LOG_FILE = "errors.csv"
MANIFEST_FILE = "manifest.csv"