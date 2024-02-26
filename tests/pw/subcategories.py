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


driver= webdriver.Chrome()
AC=ActionChains(driver)
wait=WebDriverWait(driver, 20)
driver.get("https://www.physiciansweekly.com/specialties/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
time.sleep(3)

category_pages=driver.find_elements(By.XPATH,"(//ul[@class='et-menu nav'])/li/a")


for cat in category_pages:

     a = cat.get_dom_attribute('href')
            
            
     if a.__contains__('https://www.physiciansweekly') :
            
      AC.key_down(Keys.CONTROL).click(cat).key_up(Keys.CONTROL).perform()
     if a==None:
             continue
    
handles =driver.window_handles


 
sumlength=[]
num = 0
for i in handles:
     driver.switch_to.window(i)
     
     try:
       
        
       
         # Handle the exception gracefully
        su=driver.find_elements(By.XPATH,"//ul[@class='et-menu nav']/li")
   
     except exceptions:
      
         print("")
         
  #subcats=wait.until(EC.presence_of_all_elements_located(su))
     def get_length_sum_of_su_elements(su):
      add=0
      for sub in su:
       #l=sub.get_dom_attribute('href')
            if sub.is_displayed():
            #if l.__contains__('https://www.physiciansweekly') :
               
              AC.key_down(Keys.CONTROL).click(sub).key_up(Keys.CONTROL).perform()
              
         
            elif sub.is_displayed() ==  None:
               continue
            add+=1  
      return add

sumlength.append(get_length_sum_of_su_elements(su))
print(sum(sumlength))
print(len(driver.window_handles))


   

             
               

             

 
     
 
          