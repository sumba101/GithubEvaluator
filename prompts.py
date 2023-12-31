import tiktoken

from thresholds import OPENAI_TOKEN_LIMIT

PROJECT_UNIQUENESS_PROMPT = ("I want you to act as a software engineer recruiter. I will provide a description and a "
                             "README file of a repository. Generate a report for the repository detailing the "
                             "uniqueness of the project. Consider factors such as the uniqueness of the project, "
                             "difficulty of implementation, the uniqueness of the idea, the uniqueness of the "
                             "implementation, the uniqueness of the features, the uniqueness of the code, and 2 more "
                             "factors of your choice. Point out examples for your report where possible. If there is "
                             "no README and no  Description, then just mention the absence of both. If there is "
                             "insufficient information, mention so in the report.")
REPO_MAP_CODE_QUALITY_PROMPT = ("I want you to act as a software engineer recruiter. I will provide a map of a "
                                "repository. The map contains a list of all the files in the repo, along with the "
                                "class, functions and symbols which are defined in each file. Callables like "
                                "functions and methods will also include their signatures. Generate a code quality "
                                "report for the repository detailing the quality and readability of the code. "
                                "Consider factors such as appropriate naming convention, clear naming of variables "
                                "and functions, usage of Class structure and encapsulation, splitting codebase across "
                                "appropriate files, how modular the code is, how easy it is to understand the code "
                                "and 2 more factors of your choice. Point out examples in report when critiquing. If "
                                "there is insufficient information, mention so in the report.")
README_READABILITY_PROMPT = ("I want you to act as a software engineer recruiter. I will provide a README file of a "
                             "repository. Generate a report for the repository detailing the quality and readability "
                             "of the README. Consider factors such as clear description of repository, readability, "
                             "use of sections, explanation for how to use/install/run the code, detailing of features "
                             "available currently and optionally features to be added in future, presence of links to "
                             "other pages, and 2 more factors of your choice. Point out examples for your report "
                             "where possible. If there is no README, then just mention the absence of a README file. "
                             "If there is insufficient information, mention so in the report.")

if __name__ == "__main__":
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    encode = encoding.encode(REPO_MAP_CODE_QUALITY_PROMPT)
    print(len(encode))
    decode = encoding.decode(encode[:OPENAI_TOKEN_LIMIT])
    print(decode)
