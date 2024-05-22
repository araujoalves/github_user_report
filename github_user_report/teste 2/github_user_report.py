import json
import unittest
from urllib import request


class User:
    def __init__(self, login, name, html_url, public_repos, followers, following, **kwargs):
        self.login = login
        self.name = name
        self.html_url = html_url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following
        # Additional attributes
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
            following=data.get('following')
        )
    return user


def get_user_repos(username: str) -> dict:
    url = f"https://api.github.com/users/{username}/repos"
    with request.urlopen(url) as response:
        repos_data = json.loads(response.read().decode())
        repos = {repo['name']: repo['html_url'] for repo in repos_data}
    return repos


def user_report(user: User, repos: dict) -> None:
    filename = f"{user.login}.txt"
    with open(filename, 'w') as file:
        file.write(f"Nome: {user.name}\n")
        file.write(f"Perfil: {user.html_url}\n")
        file.write(f"Número de repositórios públicos: {user.public_repos}\n")
        file.write(f"Número de seguidores: {user.followers}\n")
        file.write(f"Número de usuários seguidos: {user.following}\n")
        file.write("Repositórios:\n")
        for repo_name, repo_url in repos.items():
            file.write(f"{repo_name}: {repo_url}\n")

    # Print to console
    print(f"Nome: {user.name}")
    print(f"Perfil: {user.html_url}")
    print(f"Número de repositórios públicos: {user.public_repos}")
    print(f"Número de seguidores: {user.followers}")
    print(f"Número de usuários seguidos: {user.following}")
    print("Repositórios:")
    for repo_name, repo_url in repos.items():
        print(f"{repo_name}: {repo_url}")


class TestMethods(unittest.TestCase):
    """Classe de testes unitários."""

    def test_user_class_has_minimal_parameters(self):
        """
        Teste unitário relativo ao primeiro passo do desafio, esse cenário
        deve ser mantido na sua resolução.
        """
        parameters = ['login', 'name', 'html_url', 'public_repos', 'followers', 'following']
        user = get_user('octocat')  # Use a sample GitHub username for testing
        for param in parameters:
            self.assertTrue(hasattr(user, param))

    def test_get_user_repos(self):
        """Teste unitário para verificar a obtenção de repositórios do usuário."""
        repos = get_user_repos('octocat')  # Use a sample GitHub username for testing
        self.assertIsInstance(repos, dict)
        for name, url in repos.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(url, str)
            self.assertTrue(url.startswith("https://github.com/"))


if __name__ == "__main__":
    # Use o seu nome de usuário do GitHub para gerar o relatório
    username = 'araujoalves'
    user = get_user(username)
    repos = get_user_repos(username)
    user_report(user, repos)
    unittest.main(argv=[''], exit=False)
