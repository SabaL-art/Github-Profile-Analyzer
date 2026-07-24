import os
# from dotenv import load_dotenv
import requests
from rich.console import Console
from rich.table import Table

# load_dotenv()
# TOKEN = os.getenv("API_TOKEN")


class Profile:
    def __init__(self):
        self._username = input("Enter Username: ")

    # request
    def check(self):
        url = f"https://api.github.com/users/{self._username}"

        # profile
        try:
            response = requests.get(url)

            if response.status_code == 200:
                self.user = response.json()
                self.display()
            elif response.status_code == 404:
                print("Could not find the user!")
            else:
                print("ERROR: ", response.status_code)
        except requests.RequestException:
            print("Couldn't connect to GitHub.")
            return
        # repo
        try:
            response = requests.get(f"{url}/repos?per_page=100")

            if response.status_code == 200:
                self.repos = response.json()
                self.display()
            elif response.status_code == 404:
                print("Could not find the user!")
            else:
                print("ERROR: ", response.status_code)
        except requests.RequestException:
            print("Couldn't connect to GitHub.")
            return

    # display results

    def display(self):
        """
        followers/following count, repo count, contributions count, most used languages
        """
        console = Console()

        # profile
        profile = Table(title="🪪 Profile Report", style="cyan")
        profile.add_column("FACTOR", style="magenta")
        profile.add_column("ON PROFILE", style="green1")

        profile.add_row("Name", self.user["name"] or "N/A")
        profile.add_row("Type", self.user["type"])
        profile.add_row("Created at", self.user["created_at"][:10])
        profile.add_row("Last Profile Update", self.user["updated_at"][:10])
        profile.add_row("Email", self.user["email"]
                        if self.user["email"] else "N/A")
        profile.add_row("Bio", self.user["bio"] if self.user["bio"] else "N/A")
        profile.add_row(
            "Company", self.user["company"] if self.user["company"] else "N/A")
        profile.add_row(
            "Location", self.user["location"] if self.user["location"] else "N/A")
        profile.add_row("Hireable", "Yes" if self.user["hireable"]
                        else "N/A" if self.user["hireable"] == None else "No")

        # stats
        stats = Table(title="📊 Statistics", style="turquoise4")
        stats.add_column("FACTOR", style="magenta")
        stats.add_column("ON PROFILE", style="green1")

        stats.add_row("Public Repos", str(self.user["public_repos"]))
        stats.add_row("Public Gists", str(self.user["public_gists"]))
        stats.add_row("Followers", str(self.user["followers"]))
        stats.add_row("Following", str(self.user["following"]))

        # repo stats
        repo = Table(title="🗃️ Repo Statistics")
        repo.add_column("FACTOR", style="magenta")
        repo.add_column("ON PROFILE", style="green1")

        for i in range(self.user["repo"]):
            ...
        repo.add_row("Total Repos", str(self.user["repo"]))
        repo.add_row("Forked Repos", str(self.user["repo"]))
        repo.add_row("Original Repos", str(self.user["repo"]))

        console.print(profile)
        console.print()
        console.print(stats)


def main():
    p = Profile()
    p.check()


if __name__ == "__main__":
    main()
