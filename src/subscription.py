class SubscriptionManager:
    def __init__(self, github_api):
        self.github_api = github_api
        self.subscriptions = []

    def add_subscription(self, repo_owner, repo_name):
        self.subscriptions.append((repo_owner, repo_name))

    def remove_subscription(self, repo_owner, repo_name):
        self.subscriptions = [
            (owner, name) for owner, name in self.subscriptions if owner != repo_owner or name != repo_name
        ]

    def get_subscribed_repos(self):
        return self.subscriptions

    def fetch_updates_for_all(self):
        updates = {}
        for owner, name in self.subscriptions:
            updates[(owner, name)] = self.github_api.get_repo_updates(owner, name)
        return updates
