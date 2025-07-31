from github import Github
from config import GITHUB_TOKEN, GITHUB_USERNAME

g = Github(GITHUB_TOKEN)

def get_github_activity():
    user = g.get_user(GITHUB_USERNAME)
    repos = user.get_repos()
    
    activity = []
    for repo in repos[:5]: 
        activity.append({
            'name': repo.name,
            'description': repo.description,
            'stars': repo.stargazers_count,
            'last_updated': repo.updated_at
        })
    
    return activity