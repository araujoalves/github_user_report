from github_utils import get_user, get_user_repos
def user_report(user, repos):
    filename = f"{user.login}.txt"
    with open(filename, 'w') as file:
        file.write(f"Nome: {user.name}\n")
        file.write(f"Perfil: {user.html_url}\n")
        file.write(f"Título: {user.title}\n")
        file.write(f"Número de repositórios públicos: {user.public_repos}\n")
        file.write(f"Número de seguidores: {user.followers}\n")
        file.write(f"Número de usuários seguidos: {user.following}\n")
        file.write("Repositórios:\n")
        for repo_name, repo_url in repos.items():
            file.write(f"{repo_name}: {repo_url}\n")

    print(f"Nome: {user.name}")
    print(f"Perfil: {user.html_url}")
    print(f"Título: {user.title}")
    print(f"Número de repositórios públicos: {user.public_repos}")
    print(f"Número de seguidores: {user.followers}")
    print(f"Número de usuários seguidos: {user.following}")
    print("Repositórios:")
    for repo_name, repo_url in repos.items():
        print(f"{repo_name}: {repo_url}")

if __name__ == "__main__":
    username = 'araujoalves'
    user = get_user(username)
    repos = get_user_repos(username)
    user_report(user, repos)
