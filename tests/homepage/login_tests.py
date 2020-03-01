from selenium import webdriver
from pages.homepage.login_page import LoginPage
import unittest
import pytest
from utilities.status import Status

@pytest.mark.usefixtures("browser_setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_login_successful(self):
        self.lp.clear_login_fields()
        self.lp.login_test("test@email.com","abcabc")
        result1 = self.lp.verify_title()
        self.ts.mark(result1,"Title Verification")
        result2 = self.lp.validate_login_successful()
        self.ts.mark_final("test_login_successful",result2,"Login Verification")

    @pytest.mark.run(order=1)
    def test_login_failed_wrong_password(self):
        self.lp.login_test("test@email.com", "abcabcbc")
        result = self.lp.validate_login_failed()
        self.ts.mark_final("test_login_failed_wrong_password",result,"Login Failed Verification")

