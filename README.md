# GitHub Profile Analyzer

A terminal-based Python application that fetches live data from the GitHub REST API and generates a detailed report for any public GitHub profile. It presents profile information, repository statistics, and programming language usage in a clean, colorful terminal interface powered by **Rich**.

Whether you're curious about your own profile or someone else's, this tool provides a quick overview of their public GitHub presence.

---

## Features

### 🪪 Profile Information

Displays important account details, including:

* Name
* Account type
* Account creation date
* Last profile update
* Public email
* Bio
* Company
* Location
* Hireable status

### 📊 GitHub Statistics

Shows key account statistics such as:

* Public repositories
* Public gists
* Followers
* Following

### 🗃️ Repository Analysis

Analyzes all available public repositories (up to 100) and reports:

* Total repositories
* Original vs. forked repositories
* Most starred repository
* Most forked repository
* Most used programming language
* Average repository size

### 💻 Programming Language Breakdown

Displays:

* Languages used across repositories
* Percentage distribution of each language
* Terminal-based visual bar chart

### 🎨 Rich Terminal Interface

Uses the **Rich** library to display colorful, easy-to-read tables directly in the terminal.

---

## Technologies Used

* Python 3
* Requests
* Rich
* GitHub REST API

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Github-Profile-Analyzer.git
cd Github-Profile-Analyzer
```

Install the required dependencies:

```bash
pip install requests rich
```

---

## Usage

Run the application:

```bash
python Profile_Analyzer.py
```

Enter a GitHub username:

```text
Enter Username: torvalds
```

The application will fetch the user's public GitHub data and generate a formatted analysis report.

---

## Sample Output

```text
🪪 Profile Report

📊 Statistics

🗃️ Repository Statistics

💻 Languages Used
```

Each section is displayed as a formatted Rich table for improved readability.

> **Tip:** Adding screenshots of the actual terminal output here will make the README much more attractive.

---

## Project Structure

```text
Github_Profile_Analyzer/
│
├── Profile_Analyzer.py
└── README.md
```

---

## Limitations

* Only public GitHub data can be analyzed.
* Repository analysis is limited to the first **100** public repositories returned by the GitHub API.
* Private repositories cannot be accessed.
* GitHub contribution graphs and contribution counts are not available through the standard GitHub REST API.
* Unauthenticated requests are subject to GitHub's public API rate limit.

---

## Future Improvements

* Personal Access Token (PAT) authentication for higher API rate limits
* Repository activity analysis
* Commit history analysis
* Repository topic analysis
* Repository creation timeline
* Export reports to JSON, CSV, or PDF
* Repository size and language charts
* AI-generated insights and recommendations
* Organization profile support
* Interactive terminal menu

---

## License

This project is licensed under the MIT License.
