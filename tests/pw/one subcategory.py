from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time
import requests
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

Service_obj= Service("C:\\Users\\Primotech\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=Service_obj)
AC=ActionChains(driver)
wait=WebDriverWait(driver, 20)
driver.get("https://www.physiciansweekly.com/category/obgyn/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
time.sleep(3)




    
handles =driver.window_handles


def get_length_sum_of_su_elements(handles): 
     
 length_sum = 0 
 num = 0
 for i in handles:
     driver.switch_to.window(i)
     
     try:
       
        
       
         # Handle the exception gracefully
        su=driver.find_elements(By.XPATH,"//ul[@class='et-menu nav']/li")
   
     except exceptions:
      
         print("")
         
  #subcats=wait.until(EC.presence_of_all_elements_located(su))
     for sub in su:
       #l=sub.get_dom_attribute('href')
            if sub.is_displayed():
            #if l.__contains__('https://www.physiciansweekly') :
               
              AC.key_down(Keys.CONTROL).click(sub).key_up(Keys.CONTROL).perform()
              num = num+1
            elif sub.is_displayed() ==  None:
               continue
 
            ELEMENT=driver.find_elements(By.XPATH,"//ul[@class='et-menu nav']/li")
            length_sum += len(ELEMENT)
 return length_sum
length_sum = get_length_sum_of_su_elements(handles)
 
   
print(length_sum)