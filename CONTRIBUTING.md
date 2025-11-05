# Contributing to YouTube Transcript Downloader

Thank you for your interest in contributing to the YouTube Transcript Downloader! This document provides guidelines and instructions for contributing to this project.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear description of the enhancement
- Use cases for the enhancement
- Any implementation ideas you might have

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure nothing is broken
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add type hints where appropriate
- Maximum line length: 100 characters
- Use f-strings for string formatting

### Documentation

- Add docstrings to all functions and classes
- Update the README.md if you change functionality
- Add comments for complex logic
- Update CHANGELOG.md for significant changes

### Testing

Before submitting a PR:
1. Run the test installation script: `python test_installation.py`
2. Test your changes with the example CSV file
3. Ensure all existing functionality still works

## 🔄 Development Workflow

1. **Setup Development Environment**
   ```bash
   git clone https://github.com/yourusername/youtubeurls.git
   cd youtubeurls
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Make Changes**
   - Create a new branch for your feature/fix
   - Write clean, documented code
   - Test your changes thoroughly

3. **Submit PR**
   - Ensure your branch is up to date with main
   - Provide a clear description of changes
   - Reference any related issues

## 🎯 Areas for Contribution

### High Priority
- Add support for playlist URLs
- Implement parallel downloading
- Add more output formats (JSON, XML, SRT)
- Improve error handling and recovery

### Medium Priority
- Create a GUI interface
- Add Docker support
- Implement caching mechanism
- Add more language support

### Low Priority
- Add unit tests
- Optimize performance
- Improve documentation
- Add more examples

## 📋 Checklist for Pull Requests

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex sections
- [ ] Documentation updated if needed
- [ ] No new warnings generated
- [ ] Tests pass successfully
- [ ] CHANGELOG.md updated

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Trolling or insulting comments
- Public or private harassment
- Publishing others' private information

## 📞 Getting Help

If you need help:
1. Check the README.md documentation
2. Search existing issues
3. Create a new issue with the "question" label
4. Be patient and respectful

## 🙏 Recognition

Contributors will be recognized in:
- The project's README.md
- Release notes
- Special mentions for significant contributions

Thank you for contributing to YouTube Transcript Downloader!