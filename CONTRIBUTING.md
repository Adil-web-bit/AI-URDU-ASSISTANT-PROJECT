# Contributing to Urdu Voice Assistant

First off, thank you for considering contributing to Urdu Voice Assistant! 🎉

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Welcome newcomers
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

**When submitting a bug report, include:**
- Clear and descriptive title
- Steps to reproduce the behavior
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, Node version, browser)
- Error messages and stack traces

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.

**When submitting an enhancement suggestion, include:**
- Clear and descriptive title
- Detailed description of the proposed functionality
- Explain why this enhancement would be useful
- List any similar features in other projects (if applicable)

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## Development Setup

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

## Coding Standards

### Python (Backend)
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for functions and classes
- Keep functions small and focused
- Write unit tests for new features

### JavaScript/React (Frontend)
- Follow Airbnb JavaScript Style Guide
- Use functional components with hooks
- Use PropTypes or TypeScript
- Keep components small and reusable
- Write meaningful component names

## Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Examples:
```
Add Urdu keyboard input support
Fix microphone permission issue on Safari
Update README with deployment instructions
```

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high code coverage

### Run Tests
```bash
# Backend
cd backend
python test_services.py

# Frontend
cd frontend
npm test
```

## Documentation

- Update README.md if needed
- Add comments for complex logic
- Update API documentation
- Include examples in documentation

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🙏
