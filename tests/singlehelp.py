from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
import time
import re
driver=webdriver.Chrome()
driver.get("https://support.google.com/")
elements=driver.find_element(By.XPATH,"(//section[@class='product-selector']//ul/li)[7]")
elements.click()
time.sleep(2)
wait=WebDriverWait(driver, 10)
modul=driver.find_element(By.XPATH,"(//li[@class='appbar-helpcenter-list__item']/a)[2]")
modul.click()
view=driver.find_element(By.XPATH,"//a[normalize-space()='View all posts']")
view.click()
time.sleep(3)
view_more= driver.find_element(By.XPATH,"//button[@class='thread-list-threads__load-more-button material2-button material2-button--hairline']")
view_more.click()
driver.refresh()


thread=driver.find_elements(By.XPATH,"//div[@class='thread-list-group']")


for thr in thread:
  try:
    
    th=thr.text
    
    
    
    
    while  not th.__contains__("Updated: This week"):
     vw=By.XPATH,"//button[@class='thread-list-threads__load-more-button material2-button material2-button--hairline']"
     WebElement.view = wait.until(EC.visibility_of_element_located(vw))
     #t=By.XPATH,"(//div[@class='thread-list-group'])"
    
     WebElement.view.click()
     time.sleep(3)
     tv=By.XPATH,"(//div[@class='thread-list-group'])"
     tt=wait.until(EC.visibility_of_all_elements_located(tv))
     
     for td in tt:
       tl=td.text
       
     
     
       if "Updated: This week" in tl:
          
         
            Week=By.XPATH,"//div/div/div/a[@class='thread-list-thread']"
            weekly=wait.until(EC.visibility_of_all_elements_located(Week))
            
            for weeks in weekly:
             we=weeks.text
             for text in we:
                match = re.search(r'Replies(\d+)', text)
    
                if match:
                 reply_value = int(match.group(1))
                 if reply_value>4:
                   print(text)
            
              
               
      
                
        
        
        
       
          
       
         
         
        
      
  except TimeoutException:
    ()