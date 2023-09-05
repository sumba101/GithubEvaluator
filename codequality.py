from utils import fetch_map, fetch_readme


class CodeQuality:
    def __init__(self, repo_name):
        self.repomap = fetch_map(repo_name)
        self.readme = fetch_readme(repo_name)

    def _evaluate_code_quality(self, repo):
        pass # Prompt GPT4 with the repo map and readability prompt

