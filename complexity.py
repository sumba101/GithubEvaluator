from thresholds import *
from utils import get_file_count


class Complexity:
    def __init__(self, repository):
        self.byte_per_lang = repository.get_languages()
        self.num_lang = len(self.byte_per_lang)
        self.num_commits = repository.get_commits().totalCount
        self.file_count = get_file_count(repository)
        # self.dependencies = get_dependencies(repository)

    def _num_lang_score(self):
        return (min(self.num_lang, NUMBER_OF_LANGUAGES_UPPER) - NUMBER_OF_LANGUAGES_LOWER) / (
                    NUMBER_OF_LANGUAGES_UPPER - NUMBER_OF_LANGUAGES_LOWER)

    def _byte_per_lang_score(self):
        score = 0
        for lang in self.byte_per_lang:
            score += (min(self.byte_per_lang[lang],
                          AMOUNT_OF_BYTES_PER_LANGUAGE_UPPER) - AMOUNT_OF_BYTES_PER_LANGUAGE_LOWER) / (
                                 AMOUNT_OF_BYTES_PER_LANGUAGE_UPPER - AMOUNT_OF_BYTES_PER_LANGUAGE_LOWER)
        return score / len(self.byte_per_lang) if len(self.byte_per_lang) > 0 else 0


    def _num_commits_score(self):
        return (min(self.num_commits, NUMBER_OF_COMMITS_UPPER) - NUMBER_OF_COMMITS_LOWER) / (
                    NUMBER_OF_COMMITS_UPPER - NUMBER_OF_COMMITS_LOWER)

    def _file_count_score(self):
        return (min(self.file_count, NUMBER_OF_FILES_UPPER) - NUMBER_OF_FILES_LOWER) / (
                    NUMBER_OF_FILES_UPPER - NUMBER_OF_FILES_LOWER)

    # def _num_dependencies_score(self):
    #     return min(len(self.dependencies),NUMBER_OF_DEPENDENCIES_UPPER)-NUMBER_OF_DEPENDENCIES_LOWER/(NUMBER_OF_DEPENDENCIES_UPPER-NUMBER_OF_DEPENDENCIES_LOWER)

    def _complexity_score(self): # simple average of all the scores
        return (
                    self._num_lang_score() + self._byte_per_lang_score() + self._num_commits_score() + self._file_count_score()) / 5  # +self._num_dependencies_score())/5
