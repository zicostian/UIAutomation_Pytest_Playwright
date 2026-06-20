from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page): # This is the constructor function
        self.page = page #self is the first parameter of the constructor function
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
        
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()