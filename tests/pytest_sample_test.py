from playwright.sync_api import Page

def test_google_title(page: Page):
    # Navigate to Google
    page.goto("https://www.google.com")

    # Verify title
    assert page.title() == "Google"

def test_example():
    assert 1 + 1 == 2