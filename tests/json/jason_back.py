import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

with open('C:\\Users\\Primotech\\Downloads\\403 links.json') as f:
    data = json.load(f)
num=0


driver = webdriver.Chrome()
wait=WebDriverWait(driver,10)
for entry in data:
    first_url = entry["Source"]
    second_url = entry["Destination"]
    driver.get(first_url)
    num=num+1
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        http=[]
        href = link.get_attribute('href')
        http.append(href)
        
        if second_url in http:
            link.click()
            
            driver.back()
            time.sleep(5)
        
        
        else:
            continue
        print(num)