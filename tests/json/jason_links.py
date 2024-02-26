import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

with open('C:\\Users\\Primotech\\Downloads\\pwtest.json') as f:
    data = json.load(f)
num=0


driver = webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get("https://preview.physiciansweekly.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys('pw@123!')
driver.find_element(By.XPATH,"//input[@type='submit']").click()
for entry in data:
  
    first_url = entry["Source"]
    second_url = entry["Destination"]
    driver.get(first_url)
    time.sleep(2)
    
    
   
    
    num=num+1
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        http=[]
        href = link.get_attribute('href')
        http.append(href)
        
        if second_url in http:
            link.send_keys(Keys.CONTROL + Keys.RETURN)
            
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        
        
        else:
            #print(f"Second URL '{second_url}' not found on page: {first_url}")
            continue
        print(num)
  
      