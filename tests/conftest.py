import pytest
from selenium import webdriver
from base.webdriverfactory import Webdriverfactory

@pytest.yield_fixture(scope="class")
def browser_setUp(request,browser):
    wdf = Webdriverfactory(browser)
    driver = wdf.get_webdriver_instance()
        
    if request.cls is not None:
        request.cls.driver = driver
        
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    

@pytest.fixture(scope="session")   
def browser(request):
    return request.config.getoption("--browser")