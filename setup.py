from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Yotube-project-templete"
AUTHOR_USER_NAME = "Shivan118"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []

setup(name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_USER_NAME,
    descritpion = "This is our first release"
    long_description= long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email = "kshivan848@gmail.com",
    packages = [SRC_REPO],
    python_requires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS
    )