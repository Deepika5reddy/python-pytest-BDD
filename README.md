Step 1: Clone the Repository
git clone https://github.com/Deepika5reddy/python-pytest-BDD.git
cd python-pytest-BDD

Step 2: Install Required Packages
Install the necessary libraries for running BDD tests, API requests, database validation, and data analysis:
pip install behave requests mysql-connector-python pandas numpy scipy
If you also want to run tests using pytest, install it as well:
pip install pytest
Step 3: Run BDD Tests with behave
behave
This will automatically find and execute all feature files in the features/ directory.
Run Tests with pytest
If your project includes any test files compatible with pytest:
pytest
