# MYPUSTAK Automation

This repository contains the automation test cases for Pustak.

## Local Setup
### Requirements
- Python 3.11

### Clone Repository
Clone this project repository to your local machine.

```sh
 git clone <repository-url>
```

### Navigate to Project Directory
```sh
cd <repository-folder>
```

### Environment Variables
#### Windows
Run the below commands to set the Mypustak username and password:
```sh
set MYPUSTAK_EMAIL=your_mypustak_email
set MYPUSTAK_PASSWORD=your_mypustak_password
```

#### macOS/Linux
Run the below commands to set the Mypustak username and password:
```sh
export MYPUSTAK_EMAIL=your_mypustak_email
export MYPUSTAK_PASSWORD=your_mypustak_password
```

## Run Mypustak Test Locally
### Installation
Run this command in the project folder to install dependencies:
```sh
pip install -r requirements.txt
```

### Running Tests
To run tests in normal mode:
```sh
pytest
```
To run tests in parallel mode:
```sh
pytest -n 2
```

### Capture Screenshots on Test Failures
Screenshots are automatically captured when a test fails and stored in the `screenshots` directory.

## Run Pustak Test using GitHub Actions
### Test Execution
Configure your GitHub repository to use GitHub Actions for automated test execution.

### Set GitHub Secrets
Ensure you add the necessary secrets (`MYPUSTAK_EMAIL` and `MYPUSTAK_PASSWORD`) in the GitHub repository settings under **Secrets**.

### Manually Trigger Tests on GitHub Actions
To manually trigger a test run using GitHub Actions:
1. Go to the **Actions** tab in your GitHub repository.
2. Select the workflow you want to run.
3. Click on the **Run workflow** button.
4. Fill in any required parameters (e.g., browser name, headless mode) if prompted.
5. Click the **Run workflow** button again to start the process.

## Test Cases Overview

### Login Tests
- `test_login_valid`: Validates login with correct credentials.
- `test_login_invalid_password`: Tests login with an incorrect password.
- `test_login_empty_email`: Ensures proper error handling for an empty email.
- `test_login_incorrect_email`: Validates error handling for an invalid email format.

### Cart Tests
- `test_cart_1`: Checks if the cart is empty after login.
- `test_cart_2`: Adds an item to the cart and verifies its presence.
- `test_cart_3`: Adds an item, increases its quantity, and checks cart status.
- `test_cart_4`: Verifies cart accessibility post-login.

### Search Tests
- `test_search_functionality`: Tests searches with different queries (valid, empty, mixed cases).
- `test_special_character_search`: Tests search functionality with special characters.

## Reporting Issues
If you encounter any issues, please open an issue in this repository with details about the problem and logs if available.

---
This repository is maintained for automation testing purposes and is subject to updates as the test cases evolve.