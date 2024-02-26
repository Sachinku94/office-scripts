import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


import time

@pytest.fixture(scope="class")
def setup(request):
    driver= webdriver.Chrome()
    request.cls.driver=driver
    driver.maximize_window
    driver.get("https://www.physiciansweekly.com/")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
    yield
    driver.close