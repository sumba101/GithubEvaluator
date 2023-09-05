import json
import os
import subprocess
import xml.etree.ElementTree as ET

from aider.repomap import RepoMap


def fetch_readme(repo_name):
    pass


def get_python_dependencies():
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    output = result.stdout
    dependencies = output.split('\n')
    return dependencies

def get_javascript_dependencies():
    with open('package.json') as f:
        data = json.load(f)
        dependencies = data.get('dependencies', {})
        return dependencies.keys()

def get_ruby_dependencies():
    dependencies = []
    with open('Gemfile.lock', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('    '):
                dependency = line.strip().split(' ')[0]
                dependencies.append(dependency)
    return dependencies

def get_java_dependencies():
    dependencies = []
    tree = ET.parse('pom.xml')
    root = tree.getroot()
    namespace = {'ns': 'http://maven.apache.org/POM/4.0.0'}
    for dependency in root.findall('.//ns:dependency', namespace):
        group_id = dependency.find('ns:groupId', namespace).text
        artifact_id = dependency.find('ns:artifactId', namespace).text
        version = dependency.find('ns:version', namespace).text
        dependencies.append(f'{group_id}:{artifact_id}:{version}')
    return dependencies
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

def get_dependencies(repository_path):
    # Clone the repository to a local directory
    # ...

    # Determine the programming language of the repository
    # ...

    # Call the appropriate function based on the programming language
    if language == 'Python':
        dependencies = get_python_dependencies()
    elif language == 'JavaScript':
        dependencies = get_javascript_dependencies()
    elif language == 'Ruby':
        dependencies = get_ruby_dependencies()
    elif language == 'Java':
        dependencies = get_java_dependencies()
    else:
        dependencies = []

    return dependencies
