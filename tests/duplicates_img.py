from selenium import webdriver

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
from selenium.common.exceptions import NoSuchAttributeException
from collections import Counter

driver=webdriver.Chrome()
AC=ActionChains(driver)
wait=WebDriverWait(driver, 20)
driver.get("https://www.physiciansweekly.com/specialties/")
driver.maximize_window()
time.sleep(3)

category_pages=driver.find_elements(By.XPATH,"(//ul[@class='et-menu nav'])/li/a")


for cat in category_pages:

     a = cat.get_dom_attribute('href')
            
            
     if a.__contains__('https://www.physiciansweekly') :
            
      AC.key_down(Keys.CONTROL).click(cat).key_up(Keys.CONTROL).perform()
     
time.sleep(20)
  
handles =driver.window_handles

for windows in handles:
      driver.switch_to.window(windows)
      divs= driver.find_elements(By.XPATH,"//div[@class='post-media']/a/img")
      img=[]
      for div in divs:
              if div.is_displayed:
                img.append(div.get_attribute('src'))
                for i in img:
                  if i<1:
                   print(i)
              else:
                continue
      
                
                
                 

                
  