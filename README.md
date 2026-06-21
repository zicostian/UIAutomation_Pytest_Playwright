# UIAutomation_Pytest_Playwright

[![Playwright Tests CI](https://github.com/zicostian/UIAutomation_Pytest_Playwright/actions/workflows/playwright.yml/badge.svg)](https://github.com/zicostian/UIAutomation_Pytest_Playwright/actions/workflows/playwright.yml)

## Description

This repository is a ready-to-use `pytest` automation framework built in Python for UI Automation testing. It follows a Page Object Model (POM) structure to improve:

- Reusability
- Readability
- Maintainability
- Clean code organization

The framework is designed for fast, easy test development with Playwright and `pytest`, using page classes to encapsulate page-specific selectors and actions.

## Setup

### Prerequisites

- Python 3.11+ installed
- Git installed (optional, for cloning the repo)
- A supported browser via Playwright

### Installation

1. Clone the repository or download the project files.
2. Create a virtual environment and install dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

### Activate virtual environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

When you are finished working, deactivate the environment:

```bash
deactivate
```

Note: Ensure you're using this project's `.venv` before running `pytest`. If the
virtualenv points to a different or missing Python interpreter, recreate it and
install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

### Run the tests

From the project root directory, run:

```bash
pytest
```

This project is already configured to generate a test report at `reports/report.html`.

To run tests and create the HTML report explicitly:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Key highlights

- Python `pytest` automation framework
- Playwright browser automation support
- Page Object Model (POM) implementation
- Reusable page objects and action methods created in the `pages/` folder
- Clean separation of page actions and test logic
- HTML report generation using `pytest-html`
- Easy-to-run commands and reusable fixtures in `conftest.py`

## Example test pattern

This example shows the POM-style test pattern used in this repository.

```python
from playwright.sync_api import Page
from pages.orangehrm_home_page import HomePage
from pages.orangehrm_login_page import LoginPage


def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    home_page.is_upgrade_button_visible()
    home_page.click_performance_link()
    home_page.click_dashboard_link()
```

### Example page object

`pages/orangehrm_login_page.py` uses a page class to wrap login actions:

```python
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
```

## Notes

- The HTML report is generated at `reports/report.html`.
- The Playwright trace files are saved under `test-results/`.
- Use the page object classes in `pages/` to keep tests clean and maintainable.
- If browser binaries are not installed, run `python -m playwright install` after setting up the virtual environment.

## Author

[Zico Agustian Rusdy](https://linkedin.com/in/zicostian)
