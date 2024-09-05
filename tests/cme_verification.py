from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests

driver = webdriver.Chrome()
AC = ActionChains(driver)
wait = WebDriverWait(driver, 20)
All_text = []
Count = 0
urls = [
    "https://www.physiciansweekly.com/category/oncology-hematology/renal-cell-carcinoma-oncology-hematology/",
    "https://www.physiciansweekly.com/category/oncology-hematology/skin-cancer-oncology-hematology/",
]


for url in urls:
    driver.get(url)
    try:
        driver.maximize_window()
    except Exception:
        ()

    paragraph = By.XPATH, "//div/h2[@class='cat-section heading-inline']"
    paragrapha = wait.until(EC.presence_of_all_elements_located(paragraph))
    for para in paragrapha:
        textT = para.text
        if textT != "CME / CE":
            All_text.append("pass")

    assert all(text == "pass" for text in All_text)
    print(All_text)
