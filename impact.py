from thresholds import *
class Impact:
    def __init__(self, repository):
        self.stars = repository.stargazers_count
        self.forks = repository.forks_count
        self.watchers = repository.watchers_count
        self.pull_requests = repository.get_pulls().totalCount
        self.issues = repository.get_issues().totalCount

    def _star_score(self):
        return max(self.stars,NUMBER_OF_STARS_UPPER)-NUMBER_OF_STARS_LOWER/(NUMBER_OF_STARS_UPPER-NUMBER_OF_STARS_LOWER)

    def _fork_score(self):
        return max(self.forks,NUMBER_OF_FORKS_UPPER)-NUMBER_OF_FORKS_LOWER/(NUMBER_OF_FORKS_UPPER-NUMBER_OF_FORKS_LOWER)

    def _watcher_score(self):
        return max(self.watchers,NUMBER_OF_WATCHERS_UPPER)-NUMBER_OF_WATCHERS_LOWER/(NUMBER_OF_WATCHERS_UPPER-NUMBER_OF_WATCHERS_LOWER)

    def _pull_request_score(self):
        return max(self.pull_requests,NUMBER_OF_PULL_REQUESTS_UPPER)-NUMBER_OF_PULL_REQUESTS_LOWER/(NUMBER_OF_PULL_REQUESTS_UPPER-NUMBER_OF_PULL_REQUESTS_LOWER)

    def _issue_score(self):
        return max(self.issues,NUMBER_OF_ISSUES_UPPER)-NUMBER_OF_ISSUES_LOWER/(NUMBER_OF_ISSUES_UPPER-NUMBER_OF_ISSUES_LOWER)

    def _impact_score(self): # simple average of all the scores
        return (self._star_score()+self._fork_score()+self._watcher_score()+self._pull_request_score()+self._issue_score())/5