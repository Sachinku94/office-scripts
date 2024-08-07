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
All_links = []
Count = 0
urls = [
    "https://oncweekly.com/effects-of-aki-in-patients-with-lung-adenocarcinoma-receiving-ici/",
    "https://oncweekly.com/efficacy-of-small-bite-closure-for-hernia-in-crc-surgery/",
    "https://oncweekly.com/enhancing-nsclc-treatment-anti-mir-155-and-standard-drugs/",
    "https://oncweekly.com/delayed-surgery-worsens-escc-after-neoadjuvant-immunotherapy/",
    "https://oncweekly.com/evaluating-surgical-treatment-in-pancreatic-neuroendocrine-tumors/",
    "https://oncweekly.com/diagnostic-and-prognostic-aspects-of-b-mcl-a-clinical-review/",
    "https://oncweekly.com/epcoritamab-monotherapy-effective-in-relapsed-fl/",
    "https://oncweekly.com/prognostic-insights-into-mibc-using-ferroptosis-and-cuproptosis/",
]

for url in urls:
    driver.get(url)
    try:
        driver.maximize_window()
    except Exception:
        ()

    paragraph = By.XPATH, "//div[@id='post-content-cstm']/p/a"
    paragrapha = wait.until(EC.presence_of_all_elements_located(paragraph))
    for para in paragrapha:
        pa = para.get_attribute("target")
        pl = para.get_attribute("href")
        All_links.append(pl)
        if pa != "_blank":
            print(pl)

        please_click = By.XPATH, "//div[@id='ad-msg-article']/p"
        click = wait.until(EC.presence_of_element_located(please_click)).text
        assert len(click) != 131 and 132

        please_clicklink = By.XPATH, "//span[@id='parent']"
        click_link = wait.until(EC.presence_of_element_located(please_clicklink))
        ca = click_link.get_attribute("target")
        ca_link = click_link.get_attribute("href")
        All_links.append(ca_link)

        if ca != None and ca != "_blank":
            print(ca)

        response = requests.get(url)

        status_code = response.status_code

        assert not status_code == 404

    for all in All_links:
        if all != None:
            response = requests.get(all)

            status_code = response.status_code

            assert not status_code == 404

            print("pass")
    Count += 1
    print(Count)
