from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import logging
import utilities.custom_logger as cl
import time
import os

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def get_by(self,locator_type):
        if locator_type == "id":
            return By.ID
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "text":
            return By.LINK_TEXT
        elif locator_type == "partial_text":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            return f"No such locatar type {locator_type}"

    def find_element(self,locator,locator_type="id"):
        try:
            by = self.get_by(locator_type)
            element = self.driver.find_element(by,locator)
            self.log.info(f"Found element using by_type {by} and locator {locator}")
            return element
        except Exception as f:
            self.log.error(f"element not found using {by} and {locator}")
            return f

    def click_element(self,locator,locator_type="id"):
        try:
            element = self.find_element(locator,locator_type)
            element.click()
            self.log.info(f"Clicked on element with locator {locator} and locator_type {locator_type}")
        except Exception as f:
            self.log.error(f)
            self.log.error(f"Cannot click on the element with locator {locator} and locator_type {locator_type}")

    def send_data(self,data,locator,locator_type="id"):
        try:
            element = self.find_element(locator,locator_type)
            element.send_keys(data)
            self.log.info(f"Sent data {data} to element with locator {locator} and locator_type {locator_type}")
        except Exception as f:
            self.log.error(f)
            self.log.error(f"Cannot send data {data} to element with locator {locator} and locator_type {locator_type}")


    def element_is_present(self,locator,locator_type="id"):
        try:
            by = self.get_by(locator_type)
            element = self.driver.find_elements(by,locator)

            if len(element) > 0:
                return True
            else:
                return False

        except Exception as f:
            self.log.error(f)
            return False

    def get_title(self):
        return self.driver.title


    def wait_for_element(self,locator,locator_type="id"):
        try:
            by = self.get_by(locator_type)
            wait = WebDriverWait(self.driver,10,poll_frequencey=1)
            element = wait.until(EC.element_to_be_clickable((by,locator)))
            self.log.info("Element appeared on the web page")
            return element
        except Exception as f:
            self.log.error(f)
            self.log.error("Element did not appear on the web page")

    def take_screenshot(self,result_message):
        """
        Takes screenshot of the current web pages
        """
        file_name = result_message + "." + str(round(time.time())) + ".png"
        screenshot_directory = "../screenshots/"
        file_path = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory,file_path)
        destination_directory = os.path.join(current_directory,screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info(f"### Screenshot saved to directory {destination_file}")
        except:
            self.log.error("### Exception Occurred")
            print_stack()
            


