# score_system
This is the UI automation for the score system

# The steps to create dir and files:
1. create cases directory to store all the test cases
2. create pages directory to store all the pages
2. create conftest.py to manage fixture(reusable pieces, such as set up and tear down), configuration
3. create constants.py to store all the constants
   use dataclass decorator(helping generate methods: __init__, __repr__ and __eq__)
4. create main.py to generate the test report

# The next steps is to create operations and test cases
1. create test_score_system.py and score_page.py
2. pip3 install pytest/requests/
3. install allure(to generate beautiful test report) 
   brew install allure 
   pip3 install allure-pytest

# run test case and generate test report