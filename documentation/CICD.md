# CI Pipeline Documentation

CI pipeline is used to ensure that code is structured and consistent. In otherwords,
linting is automated, tests are ran on major components such as DJango backend, sudoko algorithm, and front end.

## Pipeline Stages

The pipeline is divided into three main stages, executed in sequential order:

1. **Lint** - This stage is responsible for checking the code for formatting and stylistic inconsistencies. (We use python black and flake8)
2. **Static Analysis** - The second stage is intended for static analysis of the code to identify potential bugs and quality issues. Currently, this stage serves as a placeholder for future static analysis implementations.
3. **Tests** - The last stage is to run all the unit tests, on backend, algorithm, and frontend to esure edits and new code does not change underlying behaviour.

## Jobs

Each stage comprises specific jobs that execute defined tasks:

### Lint Stage

- **Job: `lint_backend`**
  - **Purpose**: Runs linting tools on the backend to ensure codinng standards and formats.
  - **Environment**: Uses `python:3` Docker image.
  - **Pre-script Task**: Installs dependencies from `requirements.txt`
  - **Scripts**:
    - Runs `black` for code formatting
    - Executes `flake8` for style guide

### Static Analysis Stage

- **Job: `static_analysis_backend`**
  - **Purpose**: See the potential bugs or quality of the code
  - **Environment**: Uses the default `python:3` image
  - **Pre-script Task**: Installs dependencies from `requirements.txt`
  - **Scripts**:
    - PYTHONPATH=backend:$PYTHONPATH mypy -p backend
    - Runs the mypy created by Django

### Tests

- **Job: `unit_test_backend`**
  - **Purpose**: Test the backend django code, and also run unit tests for algorithms
  - **Environment**: Uses the default `python` image
  - **Pre-script Task**: Installs dependencies from `requirements.txt`
  - **Scripts**:
    - Run coverage script on the code for the algorithms and the django backend
    - Display the results of this

## How to run the pipelines

To run the given commands individually you can use: `sh runner.sh <job>`
And choose from the given job list
`jobs:`

- lint_backend
- lint_frontend
- static_analysis_backend
- unit_test_backend

For example:
Say you want to run the unit tests you would do:
`sh runner.sh lint_backend`
