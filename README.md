# GitHub Profile Analyzer

A terminal-based Python application that fetches and analyzes a GitHub user's public profile using the GitHub REST API. The program generates a clean, colorful report with profile information, repository statistics, and programming language usage.

## Features

* 📄 Displays profile information

  * Name
  * Account type
  * Account creation date
  * Last profile update
  * Email (if public)
  * Bio
  * Company
  * Location
  * Hireable status

* 📊 Displays GitHub statistics

  * Public repositories
  * Public gists
  * Followers
  * Following

* 🗃️ Repository analysis

  * Total repositories
  * Original vs forked repositories
  * Most starred repository
  * Most forked repository
  * Most used programming language
  * Average repository size

* 💻 Programming language report

  * Languages used across repositories
  * Percentage distribution
  * Visual bar chart in the terminal

* 🎨 Rich terminal interface using the `rich` library.

## Technologies Used

* Python 3
* Requests
* Rich
* GitHub REST API

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Github-Profile-Analyzer.git
cd Github-Profile-Analyzer
```

Install the required packages:

```bash
pip install requests rich
```

## Usage

Run the program:

```bash
python Profile_Analyzer.py
```

Enter a GitHub username when prompted:

```text
Enter Username: torvalds
```

The program will retrieve the user's public information and display a detailed report.

## Sample Output

```text
🪪 Profile Report
📊 Statistics
🗃️ Repo Statistics
💻 Languages Used
```

Each section is displayed in a formatted Rich table for better readability.

## Project Structure

```text
Github_Profile_Analyzer/
│
├── Profile_Analyzer.py
└── README.md
```

## Limitations

* Only analyzes **public** GitHub information.
* Repository analysis is limited to the first 100 public repositories.
* Private repositories are not accessible.
* GitHub contribution graphs (green squares) are not available through the standard GitHub REST API.

## Possible Future Improvements

* Authentication using a Personal Access Token to increase API rate limits.
* Repository activity analysis.
* Contribution statistics.
* Repository topic analysis.
* Commit frequency analysis.
* Export reports to PDF or CSV.
* AI-generated profile insights and recommendations.
* Repository language charts using Rich progress bars.

## License

This project is open source and available under the MIT License.
