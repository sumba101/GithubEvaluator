import os
import shutil

from dotenv import load_dotenv
from git import Repo
from github import Github

from codequality import CodeQuality
from complexity import Complexity
from impact import Impact
from unique import Unique

if __name__ == '__main__':
    # username = sys.argv[1]
    # Create a GitHub instance using an access token
    load_dotenv()
    access_token = os.environ.get('GITHUB_TOKEN')
    g = Github(access_token)

    username = "flightlesstux"
    user = g.get_user(username)
    # First we find the impact and complexity score of all the repositories
    # Then we select top 5 repositories with the highest impact and complexity score
    # Then we find code quality and unique factors for each of the top 5 repositories

    repository_score_to_repo = []
    for repository in user.get_repos():
        print(repository.name)
        # Prune out repositories that are forks
        if repository.fork or repository.visibility != "public":
            continue
        complexity = Complexity(repository)
        complexity_score = complexity._complexity_score()
        print(f"Complexity score: {complexity_score}")
        impact = Impact(repository)
        impact_score = impact._impact_score()
        print(f"Impact score: {impact_score}")
        repository_score_to_repo.append((complexity_score + impact_score, repository))
    repository_score_to_repo.sort(reverse=True)
    # iterate through the first 5 repositories
    report_card = dict()
    for i in range(5):
        repository = repository_score_to_repo[i][1]
        # clone the repository and delete afterward
        Repo.clone_from(repository.clone_url, repository.name)
        codequality = CodeQuality(repository.name)

        description = repository.description
        readme = repository.get_readme().decoded_content

        unique = Unique(description, readme)
        report_card[repository.name] = dict()
        report_card[repository.name]["code_quality"] = codequality._evaluate_code_quality(repository)
        report_card[repository.name]["unique_factors"] = unique._evaluate_code_unique(repository)

        # delete the repository
        shutil.rmtree(repository.name)

    print(report_card)