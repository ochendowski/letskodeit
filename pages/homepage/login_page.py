from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl

class LoginPage(SeleniumDriver):

    logger = cl.customLogger(logging.INFO)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    login_link = "Login"
    email_field = "user_email"
    password_field = "user_password"
    login_button = "commit"

    # action methods
    def click_login_link(self):
        self.click_element(self.login_link,"text")

    def enter_email(self,email):
        self.send_data(email,self.email_field)

    def enter_password(self,password):
        self.send_data(password,self.password_field)

    def click_login_button(self):
        self.click_element(self.login_button,"name")

    # functionality test
    def login_test(self,email="",password=""):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def validate_login_successful(self):
        result = self.element_is_present("//span[text()='Test User']","xpath")
        return result

    def validate_login_failed(self):
        result = self.element_is_present("//div[contains(text(),'Invalid email or password')]","xpath")
        return result

    def clear_login_fields(self):
        email = self.find_element(self.email_field)
        email.clear()
        password = self.find_element(self.password_field)
        password.clear()

    def verify_title(self):
        if self.get_title() == "Google":
            return True
        else:
            return False






