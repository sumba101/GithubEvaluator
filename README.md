# GithubEvaluator
Given a github link to a github user, evaluate all the repos present and select the most complex ones with adequate GPT4 explanation for choice

# Metrics to cover
The intention of complexity analysed is for gauging the person's coding capability. Hence, we shall not be exploring metrics that measure complexity of code from a maintainability/readability standpoint such as cyclometric or cognitive complexity.

The following are possible metrics:
* Public validation:
  * Number of stars
  * Number of forks
  * Number of watchers
  * Number of pull requests
* Code properties:
  * Number of dependencies/libraries used for the project (More dependencies needed, more complex processes)
  * Number of programming languages used (more languages means more complex project)
  * Number of commits (more commits means more work done on the project)
* Code structure:
  * Number of lines
  * Number of files
  * Number of functions
  * GPT4 analysis on structural complexity

Weighted score of all these categories together comprises the final score for code complexity.
