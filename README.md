# GitHub Profile Analyzer

A terminal-based GitHub Profile Analyzer built in Python.

Analyze any public GitHub profile using the GitHub REST API and view useful statistics about the user. This project is currently under development and new features will be added over time.

> **Status:** 🚧 Work in Progress

## Current Features

- Search any public GitHub user
- Fetch profile information using the GitHub API
- Error handling for invalid usernames
- API authentication using a Personal Access Token stored in a `.env` file

## Planned Features

- Profile summary
- Followers and following count
- Public repository count
- Most-used programming languages
- Repository statistics
- Account age
- Contribution analysis
- Top repositories
- Repository size statistics
- Fork and star statistics
- Rich terminal tables
- Profile score
- Export report to JSON or CSV

## Requirements

- Python 3.10+
- requests
- python-dotenv
- rich

## Installation

Install the required dependencies:

```bash
pip install requests python-dotenv rich
```

## Setup

Create a `.env` file in the project directory:

```env
API_TOKEN=YOUR_GITHUB_PERSONAL_ACCESS_TOKEN
```

Replace `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` with your GitHub Personal Access Token.

## Run

```bash
python3 Profile_Analyzer.py
```

## Usage

```text
Enter Username:
```

Example:

```text
Enter Username: torvalds
```

The program will fetch the user's public GitHub profile and display the available information.

## Project Structure

```text
GitHub_Profile_Analyzer/
├── Profile_Analyzer.py
├── .env
└── README.md
```

## Concepts Practiced

- REST APIs
- HTTP requests
- JSON parsing
- Environment variables
- Object-Oriented Programming (OOP)
- Terminal applications
- Error handling
- Working with external APIs

## Future Improvements

- Beautiful terminal UI with Rich
- Repository language charts
- Commit and contribution analysis
- User activity timeline
- Profile comparison
- Organization support
- Repository filtering
- README analysis
- Markdown/PDF report generation
- GitHub badge generation

## Author

Sabal