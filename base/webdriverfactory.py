"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver

class Webdriverfactory():

    def __init__(self,browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
         """
        self.browser = browser

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def get_webdriver_instance(self):
        """
            Get WebDriver Instance based on the browser configuration

            Returns:
            'WebDriver Instance'
        """
        url = "https://learn.letskodeit.com/"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "safari":
            driver = webdriver.Safari()
        else:
            driver = webdriver.Chrome()
        # Setting driver implicit timeout for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(url)

        return driver



