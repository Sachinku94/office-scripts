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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import inspect
import logging
import requests
import asyncio
import aiohttp

driver = webdriver.Chrome()
AC = ActionChains(driver)
wait = WebDriverWait(driver, 20)
All_links = []
Count = 0
urls = [
    "https://oncweekly.com/datopotamab-deruxtecan-vs-chemotherapy-for-hr-her2-breast-cancer/"
]


def verify_linkscloud(selectors):
    all_links = []
    log = logging.getLogger()

    for selector in selectors:
        elements = driver.find_elements(By.XPATH, selector)
        links = [element.get_attribute("href") for element in elements]
        all_links.extend(links)

    result_broken = []

    for link in all_links:
        response = requests.get(link)
        status_code = response.status_code
        if status_code == 404:

            result_broken.append("fail")
            log.info(f"Link {link} is broken with status code {status_code}")

        elif status_code != 404:
            result_broken.append("pass")

    assert all(element == "pass" for element in result_broken)


async def check_link(session, link, log):
    try:
        async with session.head(link) as response:  # Using HEAD request
            status_code = response.status
            if status_code == 404:
                log.info(f"Link {link} is broken with status code {status_code}")
                return "fail"
            else:
                return "pass"
    except Exception as e:
        log.error(f"Error checking link {link}: {e}")
        return "fail"


# Define the asynchronous function to verify all links
async def verify_links_async(selectors):
    all_links = []
    log = logging.getLogger()

    # Extract links using the provided selectors
    for selector in selectors:
        elements = driver.find_elements(By.XPATH, selector)
        links = [
            element.get_attribute("href")
            for element in elements
            if element.get_attribute("href")
        ]
        all_links.extend(links)

    # Check links asynchronously
    async with aiohttp.ClientSession() as session:

        tasks = [check_link(session, link, log) for link in all_links]
        results = await asyncio.gather(*tasks)

    # Verify if all links are okay
    assert all(result == "pass" for result in results), "Some links are broken."


for url in urls:
    driver.get(url)
    try:
        driver.maximize_window()
    except Exception:
        ()

selectors = ["//div[@id='post-content-cstm']/p/a"]
asyncio.run(verify_links_async(selectors))
