import setuptools

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define package version
__version__ = "0.0.0"

# Define repository and author details
REPO_NAME = "pics_classification_ml_Project"
AUTHOR_USER_NAME = 'PremK'
SRC_REPO = "picClassifier"
AUTHOR_EMAIL = "test@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for PIC app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Corrected the key from 'scr' to 'src'
    packages=setuptools.find_packages(where="src")
)
