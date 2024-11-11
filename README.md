# My Own Cookiecutter template

Just a simple cookiecutter remplate that I can use to generate a project quickly
with the following characteristics:

1. Use SRC-layout
2. Use poetry to manage dependencies and for virtual environment creation
3. Install my most used development dependencies
   1. bandit
   2. flake8
   3. flake8-import-order
   4. flake8-pyproject
   5. mypy
   6. pytest
   7. pytest-cov
   8. pytest-mock
   9. sphinx
   10. sphinx-rtd-theme
4. Configure pycharm with my most used run-configurations
   1. Running bandit
   2. Running flake8
   3. Running mypy
   4. Running test folder
   5. Running QA (bandit, flake8, mypy)
5. Configure flake8, bandit and mypy on pyproject.toml 
6. Add License (always MIT)
7. Add Contributing file
8. Add Notice file (empty)
9. Add .gitignore
10. Add an empty readme
11. Create a git repository and creates an initial commit based on the default
    files that are included
12. Add an empty conftest.py
 

