# Python Package Template

![Python](https://img.shields.io/badge/python-3.12-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/ref-Documentation-blue)](https://google.com)

Use this template to create a custom Python package.

## Installation

For the latest stable version, install from [PyPi](https://pypi.org/project/mypackage/):

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the package from PyPi
pip install {MY_PACKAGE}
```

## Usage

```python
import {MY_PACKAGE} as mp
```

## Development

To contribute to the development of {MY_PACKAGE}, clone the repository and install the development dependencies.

### Install the Development Dependencies

```bash
# Clone the repository
git clone https://github.com/malill/{MY_PACKAGE}.git

# Create a virtual environment
python -m venv .venv

# Install the development dependencies
pip install -r requirements-dev.txt

# Install the package in editable mode
pip install -e .
```

### Use pre-commit hooks

The pre-commit hooks are used to ensure that the code is formatted correctly and that the tests pass before committing the code.

```bash
# Install the pre-commit package
pre-commit install

# (To locally) Run the pre-commit hooks
pre-commit run --all-files
```

### Run Code Coverage

You can test the code coverage by running the following command:

```bash
# Run the code coverage
pytest --cov={MY_PACKAGE} --cov-report=html
```

This will generate a HTML report in the `htmlcov` folder. Inspect the report by opening the `index.html` file in your browser.
