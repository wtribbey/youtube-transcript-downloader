# YouTube Transcript Downloader

A Python tool for bulk downloading and processing YouTube video transcripts. This tool is designed to extract transcripts from YouTube channels for analysis, particularly useful for educational content, trading tutorials, and content research.

## 🚀 Features

- **Bulk transcript extraction** from YouTube videos via CSV input
- **Dual extraction methods**: Primary API method with yt-dlp fallback
- **Smart duplicate removal** in transcripts
- **Timestamp preservation** options
- **Error handling** with detailed logging
- **Rate limiting** to avoid API restrictions
- **Cookie support** for accessing restricted content
- **Batch processing** with progress tracking

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtubeurls.git
cd youtubeurls
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
youtubeurls/
│
├── get_channel_transcripts.py  # Main transcript downloader
├── clean_transcripts.py        # Transcript cleaning utility
├── youtubecheck.py             # Single video test script
├── transcripts/                # Output directory for transcripts
│   ├── *.txt                   # Individual transcript files
│   ├── manifest.csv            # Summary of processed videos
│   └── errors.csv              # Failed downloads log
├── *.csv                       # Input CSV files with video URLs
└── docs/                       # Documentation
```

## 💡 Usage

### Basic Usage

1. **Prepare your CSV file** with YouTube video URLs:
```csv
"Title","Date","URL"
"Video Title 1","2024-01-01","https://www.youtube.com/watch?v=VIDEO_ID1"
"Video Title 2","2024-01-02","https://www.youtube.com/watch?v=VIDEO_ID2"
```

2. **Run the transcript downloader**:
```bash
python get_channel_transcripts.py --csv your_videos.csv
```

### Advanced Options

```bash
# Include timestamps in transcripts
python get_channel_transcripts.py --csv videos.csv --with-timestamps

# Custom output directory
python get_channel_transcripts.py --csv videos.csv --out custom_transcripts

# Use browser cookies (for restricted content)
python get_channel_transcripts.py --csv videos.csv --cookies-from-browser chrome

# Adjust rate limiting (seconds between requests)
python get_channel_transcripts.py --csv videos.csv --rate-limit 1.0
```

### Clean Transcripts

Remove duplicate lines from downloaded transcripts:

```bash
# Basic cleaning (removes consecutive duplicates)
python clean_transcripts.py --root transcripts

# Create backups before cleaning
python clean_transcripts.py --root transcripts --backup

# Global deduplication (removes all duplicates, not just consecutive)
python clean_transcripts.py --root transcripts --global-dedup

# Dry run (preview changes without modifying files)
python clean_transcripts.py --root transcripts --dry-run
```

### Test Single Video

Test transcript extraction for a single video:

```bash
# Edit video_id in youtubecheck.py, then run:
python youtubecheck.py
```

## 📊 CSV Format

The input CSV can have various formats. The script intelligently detects columns:

**Minimal format** (URL only):
```csv
https://www.youtube.com/watch?v=VIDEO_ID1
https://www.youtube.com/watch?v=VIDEO_ID2
```

**Standard format** (with metadata):
```csv
Title,Date,URL
"Video Title","2024-01-01","https://www.youtube.com/watch?v=VIDEO_ID"
```

**Supported column names** (case-insensitive):
- URL columns: `url`, `link`, `video`, `video_url`
- Title column: `title`
- Date column: `date`

## 🔍 How It Works

1. **Extraction Process**:
   - Reads video URLs from CSV
   - Attempts transcript extraction via `youtube-transcript-api`
   - Falls back to `yt-dlp` if API fails
   - Handles multiple subtitle formats (en, en-US, en-GB)

2. **Output Format**:
   - Each transcript saved as `XXXX_Video_Title.txt`
   - Includes metadata header (title, URL, video ID, date)
   - Optionally includes timestamps for each text segment

3. **Error Handling**:
   - Failed downloads logged to `errors.csv`
   - Successful downloads tracked in `manifest.csv`
   - Graceful handling of missing transcripts

## 📈 Use Cases

- **Educational Content Analysis**: Extract transcripts from educational channels
- **Trading Strategy Research**: Analyze trading tutorial content (as shown in sample data)
- **Content Creation**: Research and reference material for content creators
- **Language Learning**: Extract subtitles for language study
- **Data Analysis**: Build datasets for NLP and text analysis projects

## ⚠️ Important Notes

- **Respect YouTube's Terms of Service**: Use responsibly and ethically
- **Rate Limiting**: Default 0.4 seconds between requests to avoid being blocked
- **Copyright**: Ensure you have permission to download and use transcript content
- **Storage**: Transcripts can accumulate significant disk space for large channels

## 🐛 Troubleshooting

### Common Issues

1. **No transcripts available**:
   - Video may not have captions enabled
   - Try using `--cookies-from-browser` for restricted content

2. **Rate limiting errors**:
   - Increase `--rate-limit` value
   - Process in smaller batches

3. **Encoding errors**:
   - Script handles UTF-8 and Latin-1 encodings automatically
   - Check transcript files for special characters

### Debug Mode

For detailed debugging, modify the script to increase verbosity or add logging statements.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is provided as-is for educational purposes. Please ensure compliance with YouTube's Terms of Service and respect content creators' rights.

## 🙏 Acknowledgments

- Built using `youtube-transcript-api` and `yt-dlp`
- Designed for educational and research purposes
- Sample data includes trading education content from JD Hyter