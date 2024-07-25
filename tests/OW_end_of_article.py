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
    "https://oncweekly.com/the-role-of-cox-2-expression-in-breast-cancer-prognosis/",
    "https://oncweekly.com/sips-predicts-traes-and-prognosis-in-escc-with-nict/",
    "https://oncweekly.com/standardizing-ptx-radiotherapy-for-elderly-escc/",
    "https://oncweekly.com/exploring-smcc-of-the-esophagus-a-center-review/",
    "https://oncweekly.com/68ga-nota-xh05-for-targeting-lag-3-in-melanoma-imaging/",
    "https://oncweekly.com/impact-of-lot-on-qol-in-pts-with-fl-real-world-data/",
    "https://oncweekly.com/gna-bap1-mutation-impact-on-protein-mrna-expression-in-um/",
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
