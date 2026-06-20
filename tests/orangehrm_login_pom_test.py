import re
from playwright.sync_api import Page, expect
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