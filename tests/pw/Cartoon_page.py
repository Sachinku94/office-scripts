from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time
import requests


Service_obj= Service("C:\\Users\\Primotech\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
Achains=ActionChains(driver)
wait=WebDriverWait(driver, 20)
driver.get("https://www.physiciansweekly.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[3]").click()
 
id = 0
while id <11:
  
    arrow=By.XPATH,"//li[@class='next arrow']"
    
    WebElement.rightarrow = wait.until(EC.visibility_of_element_located(arrow))
      
    WebElement.rightarrow.click() 
     
    id = id +1
    
   

    links = driver.find_elements(By.TAG_NAME, 'a')
    
    
    for link in links:
        
     a =link.get_dom_attribute('href')
    if a is None:
        continue
    
    
    r = requests.head(a)
    time.sleep(5)
            
    if r.status_code > 200:
        print("Page number",id,a, r.status_code)