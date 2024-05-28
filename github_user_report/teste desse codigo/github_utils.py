import json
from urllib import request

class User:
    def __init__(self, login, name, html_url, public_repos, followers, following, title="Test Automation Developer Analyst", **kwargs):
        self.login = login
        self.name = name
        self.html_url = html_url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following
        self.title = title

        for key, value in kwargs.items():
            setattr(self, key, value)

def get_user(username: str) -> User:
    url = f"https://api.github.com/users/{username}"
    with request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        user = User(
            login=data.get('login'),
            name=data.get('name'),
            html_url=data.get('html_url'),
            public_repos=data.get('public_repos'),
            followers=data.get('followers'),
            following=data.get('following'),
            title="Test Automation Developer Analyst"
        )
    return user

def get_user_repos(username: str) -> dict:
    url = f"https://api.github.com/users/{username}/repos"
    with request.urlopen(url) as response:
        repos_data = json.loads(response.read().decode())
        repos = {repo['name']: repo['html_url'] for repo in repos_data}
    return repos
