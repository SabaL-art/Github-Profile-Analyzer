import requests
from rich.console import Console
from rich.table import Table
from datetime import date

# ==============================================================================================================
# Max score: ( MAX=100 )
# profile= 25
# stats= 20
# repo= 55
# ==============================================================================================================


class Profile:
    def __init__(self):
        self._username = input("Enter Username: ")
        self.console = Console()

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
                self.display_results()
                self.display_score()
            elif response2.status_code == 404:
                print("Could not find the user!")
            else:
                print("ERROR: ", response2.status_code)
        except requests.RequestException:
            print("Couldn't connect to GitHub.")
            return

    # =========== Profile report ===========

    def profile_score(self):
        score = 0
        # for account age
        created = (self.user["created_at"][:10]).split("-")
        created_date = date(int(created[0]), int(created[1]), int(created[2]))
        account_age = (date.today()-created_date).days
        self.account_age = account_age
        # for last update
        updated = (self.user["updated_at"][:10]).split("-")
        updated_date = date(int(updated[0]), int(updated[1]), int(updated[2]))
        last_update = (date.today() - updated_date).days
        # -score LAST UPDATE-
        ratio = last_update / max(account_age, 1)
        if ratio <= 0.05:
            score += 10
        elif ratio <= 0.10:
            score += 8
        elif ratio <= 0.25:
            score += 6
        elif ratio <= 0.50:
            score += 3
        else:
            score += 0
        # -score NAME-
        score += 3 if self.user["name"] else 0
        # -score EMAIL-
        score += 2 if self.user["email"] else 0
        # -score BIO-
        score += 5 if self.user["bio"] else 0
        # -score LOCATION-
        score += 2 if self.user["location"] else 0
        # -score HIREABLE-
        score += 0 if self.user["hireable"] == None else 3

        return score

    def profile_Table(self):
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
        return profile

    # =========== Statistics report ===========

    def stats_score(self):
        score = 0
        followers = self.user["followers"]
        following = self.user["following"]
        # -score POPULARITY-
        if followers >= 1000:
            score += 8
        elif followers >= 500:
            score += 7
        elif followers >= 200:
            score += 6
        elif followers >= 100:
            score += 5
        elif followers >= 50:
            score += 4
        elif followers >= 20:
            score += 3
        elif followers >= 5:
            score += 2
        elif followers >= 1:
            score += 1

        if following > 0:
            ratio = followers / following

            if ratio >= 5:
                score += 2
            elif ratio >= 2:
                score += 1
        # -score REPOS-
        repos = self.user["public_repos"]
        if repos >= 5:
            score += 5
        else:
            score += repos

        # -score GISTS-
        gists = self.user["public_gists"]
        if gists >= 5:
            score += 5
        else:
            score += gists

        return score

    def stats_Table(self):
        stats = Table(title="📊 Statistics", style="turquoise4")
        stats.add_column("FACTOR", style="magenta")
        stats.add_column("ON PROFILE", style="green1")

        stats.add_row("Public Repos", str(self.user["public_repos"]))
        stats.add_row("Public Gists", str(self.user["public_gists"]))
        stats.add_row("Followers", str(self.user["followers"]))
        stats.add_row("Following", str(self.user["following"]))

        return stats

    # =========== Repo report ===========

    def repo_score(self):
        score = 0
        total_repo = self.user["public_repos"]
        original_repo = total_repo-self.forks

        # -score REPOS/YEAR-
        if total_repo == 0:
            score = 0
        else:
            repo_per_year = total_repo/(max(self.account_age, 1)/365)
            if repo_per_year >= 10:
                score += 10
            else:
                score += round(repo_per_year)

            # -score ORIGINAL REPOS-
            original_repo_ratio = original_repo/total_repo
            if original_repo_ratio == 1:
                score += 10
            elif original_repo_ratio >= 0.8:
                score += 7
            elif original_repo_ratio >= 0.5:
                score += 4
            else:
                score += 0

            # -score MOST STARRED REPO-
            stars = self.most_starred["total_stars"]
            if stars == 0:
                score += 0
            elif stars < 5:
                score += 2
            elif stars < 10:
                score += 4
            elif stars < 25:
                score += 6
            elif stars < 50:
                score += 8
            elif stars < 100:
                score += 9
            else:
                score += 10

            # -score MOST FORKED REPO-
            forks = self.most_forked["total_forks"]
            if forks == 0:
                score += 0
            elif forks <= 2:
                score += 2
            elif forks <= 4:
                score += 5
            elif forks <= 10:
                score += 7
            elif forks <= 15:
                score += 8
            else:
                score += 10

            languages = self.languages
            if len(languages) == 0:
                score += 0
            elif len(languages) < 2:
                score += 4
            elif len(languages) < 3:
                score += 6
            elif len(languages) < 4:
                score += 9
            elif len(languages) < 5:
                score += 12
            else:
                score += 15

        return score

    def repo_Table(self):
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

        self.most_forked = most_forked
        self.most_starred = most_starred
        self.forks = forks
        self.languages = languages
        return repo

    # =========== Languages report ===========

    def language_Table(self):
        languages = self.languages
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
        return lang

    # display results
    def display_results(self):
        """
        followers/following count, repo count, contributions count, most used languages
        """
        # =========== profile ===========
        profile = self.profile_Table()
        # =========== stats ===========
        stats = self.stats_Table()
        # =========== repo stats ===========
        repo = self.repo_Table()
        # =========== languages used ===========
        lang = self.language_Table()
        # =========== display the tables ===========
        self.console.print(profile)
        self.console.print()
        self.console.print(stats)
        self.console.print()
        self.console.print(repo)
        self.console.print()
        self.console.print(lang)

    # display score
    def display_score(self):
        profile = self.profile_score()
        stats = self.stats_score()
        repo = self.repo_score()
        total = profile+stats+repo
        print("============ SCORES ============")
        print(f"PROFILE SCORE: {profile}/25")
        print(f"STATS SCORE: {stats}/20")
        print(f"REPO SCORE: {repo}/55")
        print(f"\nTOTAL SCORE= {total}/100")
        print()
        if total >= 90:
            print("🏆 Outstanding")
            print(
                "Exceptional GitHub profile with high-quality projects and strong activity.")
        elif total >= 80:
            print("🌟 Excellent")
            print("Strong profile with good repositories and an active presence.")
        elif total >= 70:
            print("⭐ Good")
            print("Well-rounded profile with solid projects and room for improvement.")
        elif total >= 60:
            print("👍 Fair")
            print("Decent profile, but improving projects or profile details would help.")
        elif total >= 50:
            print("🌱 Beginner")
            print("Good start, but needs more original repositories and activity.")
        elif total >= 40:
            print("🚀 Getting Started")
            print("Early-stage GitHub profile. Keep building and sharing projects.")
        elif total >= 20:
            print("📝 Incomplete")
            print("Very little public activity or profile information available.")


def main():
    p = Profile()
    p.check()


if __name__ == "__main__":
    main()
