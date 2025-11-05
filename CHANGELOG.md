# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-20

### Added
- Initial release of YouTube Transcript Downloader
- Core transcript extraction functionality using youtube-transcript-api
- Fallback support using yt-dlp for videos where API fails
- Batch processing from CSV files
- Transcript cleaning utility to remove duplicates
- Support for timestamps in transcripts
- Cookie support for accessing restricted content
- Rate limiting to avoid API restrictions
- Progress tracking with tqdm
- Comprehensive error logging
- Manifest file generation for tracking successful downloads

### Features
- Multiple input CSV formats supported
- Intelligent column detection
- Safe filename generation from video titles
- UTF-8 and Latin-1 encoding support
- Configurable output directory
- Browser cookie integration (Chrome, Firefox, Edge, Brave)

### Documentation
- Comprehensive README with usage examples
- Example CSV file for testing
- MIT License
- Configuration file for centralized settings

## [Unreleased]

### Planned Features
- Support for playlist URLs
- Multi-language transcript support
- Export to different formats (JSON, XML, SRT)
- Parallel processing for faster downloads
- GUI interface
- Docker containerization
- API endpoint for web service deployment