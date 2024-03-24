import requests

def fetch_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f"Failed to fetch repositories for user '{username}'. Status code: {response.status_code}")
        return None

def display_repository_info(repositories):
    if repositories:
        print("Repository Information:")
        for repo in repositories:
            name = repo.get("name")
            description = repo.get("description")
            language = repo.get("language")
            stars = repo.get("stargazers_count")
            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Language: {language}")
            print(f"Stars: {stars}")
            print("-" * 30)
    else:
        print("No repository information available.")

def main():
    username = input("Enter GitHub username: ")
    repositories = fetch_user_repositories(username)
    if repositories:
        display_repository_info(repositories)

if __name__ == "__main__":
    main()
