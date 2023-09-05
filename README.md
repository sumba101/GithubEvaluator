# GithubEvaluator
Given a github link to a github user, evaluate all the repos present and select the most complex ones with adequate GPT4 explanation for choice

# Metrics to cover
Given a repository, we want to evaluate Complexity, Code Quality, Useful/Impactful-ness, Uniqueness/Toughness a repository is 

The following are possible metrics:
* Complexity:
  * Number of languages
  * Amount of bytes per language
  * Number of dependencies
  * Number of files
  * Number of commits
  The above metrics can be made into numeric scores each by making use of defined lower and upper thresholds for each metric. The final score can be a weighted sum of all these scores.
* Code Quality:
  * Repository Map
  * Readability of ReadMe
  These two can be arrived upon by using GPT4 to generate a score for each of these. 
* Useful/Impactful-ness:
  * Number of stars
  * Number of forks
  * Number of watchers
  * Number of pull requests
  * Number of issues
  Like with complexity, we shall set thresholds for each of these and arrive at a score for each of these.
* Uniqueness/Toughness:
  * ReadMe + Description 
  This is a subjective metric and can be arrived at by using GPT4 to generate a text evaluation for each metric. 

The goal would be to generate the Uniqueness/Toughness and Code Quality evaluations with GPT4 for the top 5 good repositories ranked using the other metrics.

# How to run
* Clone the repo
* Install the requirements using `pip install -r requirements.txt`
* Run the script using `python main.py`

