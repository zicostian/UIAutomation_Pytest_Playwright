import re # re is for regrex (used in title check)
from playwright.sync_api import expect, Page

def test_google_seaarch(page):
    # Navigate to Google
    page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page is fully loaded
    page.goto("https://www.google.com/ncr")
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup found, continuing with the test.")
        
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")

    # Verify title
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))