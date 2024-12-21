import requests

class GitHubAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_repo_updates(self, repo_owner, repo_name):
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/events"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_commit_history(self, repo_owner, repo_name):
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
