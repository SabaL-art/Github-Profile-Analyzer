import os
from dotenv import load_dotenv
import requests
from rich.console import Console
from rich.table import Table

load_dotenv()
TOKEN = os.getenv("API_TOKEN")


class profile:
    def __init__(self):
        self._username = input("Enter Username: ")

    # request
    def check(self):
        url = f"https://api.github.com/users/{self._username}"
        response = requests.get(url)

        if response.status_code == 200:
            self.user = response.json()
            self.display()
        elif response.status_code == 404:
            print("Could not find the user!")
        else:
            print("ERROR: ", response.status_code)

    # display results
    def display(self):
        """
        followers/following count, repo count, contributions count, most used languages,  
        """
        print(self.user)


def main():
    p = profile()
    p.check()


if __name__ == "__main__":
    main()
