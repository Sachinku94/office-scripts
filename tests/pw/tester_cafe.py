from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time
import requests


Service_obj= Service("C:\\Users\\Primotech\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
AC=ActionChains(driver)
wait=WebDriverWait(driver, 20)

driver.get("https://www.testerscafe.in/")


driver.maximize_window()

    
   


'''links = driver.find_elements(By.TAG_NAME, 'a')

   
for link in links:
   try:
        
    a =link.get_attribute('href')
    
    
    if a.__eq__("#"):
            continue
       
        
            
    
    print(a)
        
    r = requests.head(a)
    time.sleep(5)
            
    if r.status_code < 400:
        print("Page number",id,a, r.status_code)
            
    img =driver.find_elements(By.XPATH,"//img")
        
    for im in img:
            if im is None:
              continue
            elif im is 'https://#':
                continue
            emg=im.get_attribute("src")
            if r.status_code > 400:
             print("Page number",id,a, r.status_code)
   except requests.exceptions.InvalidSchema:
    continue'''
hover=driver.find_element(By.XPATH,"//a[contains(.,'Company')]")

li=driver.find_elements(By.XPATH,"(//ul[@class='dropdown-menu'][1])[1]/li")

for i in li:
    AC.move_to_element(hover)
    time.sleep(1)
    a =i.get_attribute('href')
    AC.key_down(Keys.CONTROL).click(i).key_up(Keys.CONTROL).perform()
            
            
            
    if a==None:
        continue
    time.sleep(3)
    
    
'''hov=driver.find_element(By.XPATH,"//a[contains(.,'Services')]")
lin=driver.find_elements(By.XPATH,"(//ul[@class='dropdown-menu'])[1]")
for l in lin :
    at=driver.find_elements(By.XPATH,"(//ul[@class='dropdown-menu'])[3]")
    AC.move_to_element(hov)
    time.sleep(2)'''
    