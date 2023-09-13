# GithubEvaluator

Given a github username, evaluate all the repositories present and select the most complex ones with adequate GPT4
reports

# Metrics to cover
Given a repository, we want to evaluate Complexity, Code Quality, Useful/Impactful-ness, Uniqueness/Toughness a repository is 

The following are possible metrics:
* Complexity:
  * Number of languages
  * Amount of bytes per language
  * Number of dependencies*
  * Number of files
  * Number of commits
  The above metrics can be made into numeric scores each by making use of defined lower and upper thresholds for each metric. The final score can be a weighted sum of all these scores.
* Code Quality:
  * Code Quality from Repository Map
  * Readability of ReadMe
    Repository Map can be used to create a comprehensive GPT4 report covering naming convention, structure, modularity
    and understandability.
    Readability of ReadMe can be evaluated using GPT4 to generate a report on the ReadMe.
* Useful/Impactful-ness:
  * Number of stars
  * Number of forks
  * Number of watchers
  * Number of pull requests
  * Number of issues
  Like with complexity, we shall set thresholds for each of these and arrive at a score for each of these.
* Uniqueness/Toughness:
  * ReadMe + Description
    This is a subjective metric and can be arrived at by using GPT4 to generate a report using README and Description to
    judge difficulty and uniqueness of the implementation .

The goal would be to generate the Uniqueness/Toughness and Code Quality evaluations with GPT4 for the top 5 good repositories ranked using the other metrics.

NOTE *: Number of dependencies function is currently commented out, must test a bit more to ensure generalisability.
# How to run
* Clone the repo
* Install the requirements using `pip install -r requirements.txt`
* Create a file `.env` and add the following lines

```
GITHUB_TOKEN='<GITHUB_TOKEN>'
OPENAI_API_KEY='<OPEN_API_KEY>'
```

To generate a github token, follow the
instructions [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

To generate an openai api key, follow the instructions [here](https://platform.openai.com/account/api-keys)

* Run the script using

```
python main.py <github_username>
```

The script will generate a folder ReportCard which will contain the reports for the top 5 repositories. The report will
contain the following for each repository:

* Complexity
* Code Quality
* Useful/Impactful-ness

# Customization

The prompts used for generating the reports can be found in the file `prompts.py`. The prompts can be modified to
generate different reports. Highly recommend playing with the prompt to get the best results.

The variables used for governing the thresholds for each metric can be found in the file `constants.py`. The variables
can be modified to govern the number of repositories selected, the weightage given to impact vs complexity and
upper-lower bounds used for generating the scores.

The token limit required to not hit maximum content length error can be found in threshold.py.

# To Note

The script will only consider code repositories that are authored by the given github user. Contributions made to other
repositories will not be considered. This includes contributions made to open source repositories.

This can be explored and implemented in the future.

# Credits

Credits to the aider module and the repomap function used goes
to [paul-gauthier](https://github.com/paul-gauthier/aider)

Checkout his explanation on how to improve GPT4 visibility of code repository using
CTags [here](https://aider.chat/docs/ctags.html)