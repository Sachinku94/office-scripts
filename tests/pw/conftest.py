import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.chrome.service import Service

import time

@pytest.fixture(scope="class")
def setup(request):
    Service_obj=Service("C:\\Users\\Primotech\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver=webdriver.Chrome(service=Service_obj)
    request.cls.driver=driver
    driver.maximize_window
    driver.get("https://www.physiciansweekly.com/")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
    yield
    driver.close