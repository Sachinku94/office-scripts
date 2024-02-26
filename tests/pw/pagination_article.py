
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
driver.get("https://www.physiciansweekly.com/category/cardiology/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
time.sleep(3)
'''driver.find_element(By.XPATH,"(//span[@class='view-all'])[2]").click()
 
id = 1
while id <423:
  
    arrow=By.XPATH,"//li[@class='next arrow']"
    
    WebElement.rightarrow = wait.until(EC.visibility_of_element_located(arrow))
      
    WebElement.rightarrow.click() 
     
    id = id +1'''
try:

 links = driver.find_elements(By.TAG_NAME, 'a')
except requests.exceptions.MissingSchema:
    print("")
    
    
for link in links:
        
        a =link.get_dom_attribute('href')
        if a is None:
            continue
        assert a.__contains__('https://staging.physiciansweekly.com')==False
            
        if a==None:
            continue
        print(a)
        r = requests.head(a)
        time.sleep(5)
            
        if r.status_code > 400:
            print("Page number",id,a, r.status_code)
    
try:
        
        img =driver.find_elements(By.XPATH,"//img")
        for im in img:
            if im is None:
              continue
            elif im is None:
                continue
            emg=im.get_attribute("src")
            if r.status_code > 400:
             print("Page number",id,a, r.status_code)
             
except requests.exceptions.MissingSchema:
        print("")
    
					
      

   