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
    "https://www.physiciansweekly.com/category/cardiology/atherosclerosis-cardiology/",
    "https://www.physiciansweekly.com/category/cardiology/atrial-fibrillation-cardiology/",
    "https://www.physiciansweekly.com/category/cardiology/hypertension-cardiology/",
    "https://www.physiciansweekly.com/category/cardiology/peripheral-artery-disease-cardiology/",
    "https://www.physiciansweekly.com/category/cardiology/stroke-cardiology/",
    "https://www.physiciansweekly.com/category/cardiology/venous-thrombosis-cardiology/",
    "https://www.physiciansweekly.com/category/endocrinology/diabetes-endocrinology/",
    "https://www.physiciansweekly.com/category/endocrinology/infertility-endocrinology/",
    "https://www.physiciansweekly.com/category/endocrinology/menopause-endocrinology/",
    "https://www.physiciansweekly.com/category/endocrinology/osteoporosis-endocrinology/",
    "https://www.physiciansweekly.com/category/primary-care/diabetes-primary-care/",
    "https://www.physiciansweekly.com/category/primary-care/diet-nutrition-primary-care/",
    "https://www.physiciansweekly.com/category/primary-care/geriatrics-primary-care/",
    "https://www.physiciansweekly.com/category/primary-care/obesity-primary-care/",
    "https://www.physiciansweekly.com/category/primary-care/smoking-tobacco-primary-care/",
    "https://www.physiciansweekly.com/category/primary-care/vaccines-primary-care/",
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
