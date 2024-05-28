import unittest
from github_utils import get_user, get_user_repos

class TestMethods(unittest.TestCase):

    def test_user_class_has_minimal_parameters(self):
        parameters = ['login', 'name', 'html_url', 'public_repos', 'followers', 'following', 'title']
        user = get_user('octocat')
        for param in parameters:
            self.assertTrue(hasattr(user, param))

    def test_get_user_repos(self):
        repos = get_user_repos('octocat')
        self.assertIsInstance(repos, dict)
        for name, url in repos.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(url, str)
            self.assertTrue(url.startswith("https://github.com/"))

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
