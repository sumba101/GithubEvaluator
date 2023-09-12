import os
import shutil
import sys

from dotenv import load_dotenv
from git import Repo
from github import Github

from codequality import CodeQuality
from complexity import Complexity
from impact import Impact
from thresholds import IMPACT_WEIGHTAGE, COMPLEXITY_WEIGHTAGE
from unique import Unique

if __name__ == '__main__':
    username = sys.argv[1]
    # Create a GitHub instance using an access token
    load_dotenv()
    access_token = os.environ.get('GITHUB_TOKEN')
    g = Github(access_token)

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
        repository_score_to_repo.append(
            (complexity_score * COMPLEXITY_WEIGHTAGE + impact_score * IMPACT_WEIGHTAGE, repository))
    repository_score_to_repo.sort(reverse=True, key=lambda x: x[0])
    # iterate through the first 5 repositories
    print("Selected top 5 repositories for code quality and unique factors")
    report_card = dict()
    for i in range(min(REPOSITORIES_TO_CONSIDER, len(repository_score_to_repo))):
        repository = repository_score_to_repo[i][1]
        # clone the repository and delete afterward
        # Check if the repository does not exist
        if not os.path.exists(repository.name):
            Repo.clone_from(repository.clone_url, repository.name)
        description = "No Description Present."
        try:
            if repository.description is not None:
                description = str(repository.description)
        except:
            pass
        readme = "No README present."
        try:
            if repository.get_readme() is not None:
                readme = str(repository.get_readme().decoded_content.strip())
        except:
            pass  # readme file doesnt exist
        print("Evaluating code quality and unique factors for repository: " + repository.name)
        codequality = CodeQuality(repository.name, readme)
        unique = Unique(description, readme)
        report_card[repository.name] = dict()
        (code_quality, resume_readability) = codequality._evaluate_code_quality()
        report_card[repository.name]["code_quality"] = code_quality
        report_card[repository.name]["readme_readability"] = resume_readability
        report_card[repository.name]["unique_factors"] = unique._evaluate_code_unique()

        # delete the directory
        shutil.rmtree(repository.name, ignore_errors=True)
        # Create a folder ReportCard if it does not exist
        if not os.path.exists("ReportCard"):
            os.mkdir("ReportCard")
        # Add a folder for the repository and in the repository folder add a file for code quality and unique factors contents
        if not os.path.exists(f"ReportCard/{repository.name}"):
            os.mkdir(f"ReportCard/{repository.name}")
        with open(f"ReportCard/{repository.name}/code_quality.txt", "w") as f:
            f.write(report_card[repository.name]["code_quality"])
        with open(f"ReportCard/{repository.name}/unique_factors.txt", "w") as f:
            f.write(report_card[repository.name]["unique_factors"])
        with open(f"ReportCard/{repository.name}/readme_readability.txt", "w") as f:
            f.write(report_card[repository.name]["readme_readability"])

    print("Report card generated.")
