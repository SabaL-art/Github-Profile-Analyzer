import os
import requests
from rich.console import Console
from rich.table import Table


class Profile:
    def __init__(self):
        self._username = input("Enter Username: ")

    # request
    def check(self):
        url = f"https://api.github.com/users/{self._username}"

        # profile
        try:
            response1 = requests.get(url)

            if response1.status_code == 200:
                self.user = response1.json()
            elif response1.status_code == 404:
                print("Could not find the user!")
            else:
                print("ERROR: ", response1.status_code)
        except requests.RequestException:
            print("Couldn't connect to GitHub.")
            return
        # repo
        try:
            response2 = requests.get(f"{url}/repos?per_page=100")

            if response2.status_code == 200:
                self.repos = response2.json()
                self.display()
            elif response2.status_code == 404:
                print("Could not find the user!")
            else:
                print("ERROR: ", response2.status_code)
        except requests.RequestException:
            print("Couldn't connect to GitHub.")
            return

    # display results
    def display(self):
        """
        followers/following count, repo count, contributions count, most used languages
        """
        console = Console()

        # =========== profile ===========
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

        # =========== stats ===========
        stats = Table(title="📊 Statistics", style="turquoise4")
        stats.add_column("FACTOR", style="magenta")
        stats.add_column("ON PROFILE", style="green1")

        stats.add_row("Public Repos", str(self.user["public_repos"]))
        stats.add_row("Public Gists", str(self.user["public_gists"]))
        stats.add_row("Followers", str(self.user["followers"]))
        stats.add_row("Following", str(self.user["following"]))

        # =========== repo stats ===========
        languages = {}
        forks = 0
        avg_size = 0
        most_forked = {
            "name": "",
            "total_forks": 0
        }
        most_starred = {
            "name": "",
            "total_stars": 0
        }

        repo = Table(title="🗃️ Repo Statistics", style="medium_purple4")
        repo.add_column("FACTOR", style="magenta")
        repo.add_column("ON PROFILE", style="green1")

        for current_repo in self.repos:

            # is forked?
            if current_repo["fork"]:
                forks += 1
                continue
            # language
            language = current_repo["language"] or "N/A"
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
            # most starred
            if current_repo["stargazers_count"] > most_starred["total_stars"]:
                most_starred["name"] = current_repo["name"]
                most_starred["total_stars"] = current_repo["stargazers_count"]
            # most forked
            if current_repo["forks_count"] > most_forked["total_forks"]:
                most_forked["name"] = current_repo["name"]
                most_forked["total_forks"] = current_repo["forks_count"]
            # avg size
            avg_size += current_repo["size"]
        try:
            avg_size /= len(self.repos)-forks
        except ZeroDivisionError:
            avg_size = 0
        # sorting for most used language
        languages = dict(
            sorted(languages.items(), key=lambda item: item[1], reverse=True))

        repo.add_row("Total Repos", str(len(self.repos)))
        repo.add_row("Forked Repos", str(forks))
        repo.add_row("Original Repos", str(len(self.repos)-forks))
        # check most_forked
        if most_forked["name"] == "":
            repo.add_row("Most Forked", "N/A")
        else:
            repo.add_row(
                "Most Forked", f"{most_forked['name']} : {most_forked['total_forks']}")
        # check most_starred
        if most_starred["name"] == "":
            repo.add_row("Most Starred", "N/A")
        else:
            repo.add_row(
                "Most Starred", f"{most_starred['name']} : {most_starred['total_stars']}")
        # check languages
        if languages:
            repo.add_row("Most Used Language", str(
                list(languages.items())[0][0]))
        else:
            repo.add_row("Most Used Language", "N/A")
        repo.add_row("Average Repo Size", f"{avg_size:.2f} KB")

        # =========== languages used ===========
        lang = Table(title="💻 Languages Used", style="bright_black")
        lang.add_column("FACTOR", style="magenta")
        lang.add_column("ON PROFILE", style="green1")

        percentage = []
        total = sum(languages.values())
        for l in languages:
            percentage.append(languages[l]*100/total)
        i = 0
        for l in languages:
            lang.add_row(
                str(l), f"{'█'*round(percentage[i]/5)} {percentage[i]:.2f}%")
            i += 1

        # =========== display the tables ===========
        console.print(profile)
        console.print()
        console.print(stats)
        console.print()
        console.print(repo)
        console.print()
        console.print(lang)


def main():
    p = Profile()
    p.check()


if __name__ == "__main__":
    main()
