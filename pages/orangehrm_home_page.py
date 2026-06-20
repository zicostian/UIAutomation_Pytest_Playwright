from playwright.sync_api import Page, expect

class HomePage:
    
    def __init__(self, page: Page):  # This is the constructor function
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        
    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible()
        
    def is_performance_link_visible(self): # From here is action methods
        expect(self.performance_link).to_be_visible()
    
    def click_performance_link(self):
        self.performance_link.click()
        
    def is_dashboard_link_visible(self):
        expect(self.dashboard_link).to_be_visible()
    
    def click_dashboard_link(self):
        self.dashboard_link.click()