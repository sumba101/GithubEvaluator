import os
import shutil

from git import Repo
from github import Github
from dotenv import load_dotenv
from aider.repomap import RepoMap


def get_file_count(repo):
    contents = repo.get_contents("")
    file_count = 0
    for content in contents:
        if content.type == "file":
            file_count += 1
    return file_count

def fetch_map(repo_name):
    other_fnames = []
    exclude_prefixes = ('__', '.')  # exclusion prefixes
    exclude_postfixes = ('.pyc', '.pyo', '.pyd','.jar','mvnw','.cmd')  # exclusion postfixes
    for root, dirs, files in os.walk(repo_name,topdown=True):
        files[:] = [f
                       for f in files
                       if not f.startswith(exclude_prefixes) and not f.endswith(exclude_postfixes)]
        dirs[:] = [dirname
                       for dirname in dirs
                       if not dirname.startswith(exclude_prefixes)]
        for file in files:
            other_fnames.append(os.path.join(root, file))
        # use files and dirs
    rm = RepoMap(root=repo_name)

    repo_map = rm.get_repo_map([], other_fnames)
    return repo_map

if __name__ == '__main__':
    # username = sys.argv[1]
    # Create a GitHub instance using an access token
    load_dotenv()
    access_token = os.environ.get('GITHUB_TOKEN')
    g = Github(access_token)

    username = "flightlesstux"
    user = g.get_user(username)
    for repository in user.get_repos():
        print(repository.name)
        # Prune out repositories that are forks
        if repository.fork or repository.visibility != "public":
            continue
        stars = repository.stargazers_count
        forks = repository.forks_count
        watchers = repository.watchers_count
        print(f'Stars: {stars}, Forks: {forks}, Watchers: {watchers}')
        default_branch = repository.default_branch

        # Get the repository's languages
        languages = repository.get_languages() # It will give dict of language to bytes of code of that language

        # Retrieve the number of programming languages used
        num_languages = len(languages)

        # Retrieve the number of commits
        num_commits = repository.get_commits().totalCount

        total_pull_requests = repository.get_pulls().totalCount

        total_issues = repository.get_issues().totalCount

        file_count = get_file_count(repository)
        # clone the repository and delete afterwards
        Repo.clone_from(repository.clone_url, repository.name)
        repo_map = fetch_map(repository.name)
        print(repo_map)
        shutil.rmtree(repository.name)