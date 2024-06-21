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

driver=webdriver.Chrome()
AC=ActionChains(driver)
wait=WebDriverWait(driver,20)
All_links=[]

url="https://oncweekly.com/esmo-gynecological-cancers-conference-2024-an-overview/"
driver.get(url)
driver.maximize_window()

paragraph=By.XPATH,"//div[@id='post-content-cstm']/p/a"
paragrapha=wait.until(EC.visibility_of_all_elements_located(paragraph))
for para in paragrapha:
    pa=para.get_attribute("target")
    pl=para.get_attribute("href")
    All_links.append(pl)
    assert pa == "_blank"
    
    
                
                 
    please_click=By.XPATH,"//div[@id='ad-msg-article']/p"
    click=wait.until(EC.visibility_of_element_located(please_click)).text
    assert len(click)!=131 and 132

    please_clicklink=By.XPATH,"//span[@id='parent']"
    click_link=wait.until(EC.visibility_of_element_located(please_clicklink))
    ca=click_link.get_attribute("target")
    ca_link=click_link.get_attribute("href")
    All_links.append(ca_link)
    
    if ca!=None:
     assert ca == "_blank"
    response = requests.get(url)


    status_code = response.status_code
          
    assert not status_code == 404 

for all in All_links:
  if all !=None:
    response = requests.get(all)


    status_code = response.status_code
          
    assert not status_code == 404 

    print("pass")

    

driver.quit()




              