
#import pytest
from utilities.Base_class import BaseClass
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
#@pytest.mark.usefixtures("setup")
class TestHomepage(BaseClass):
    def test_PW(self):
        wait=WebDriverWait(self.driver, 20)
        self.driver.find_element(By.XPATH,"(//span[@class='view-all']/a)[1]").click()
        time.sleep(3)
        id = 0
        while id <5:
  
            arrow=By.XPATH,"//li[@class='next arrow']"
    
            WebElement.rightarrow = wait.until(EC.visibility_of_element_located(arrow))
      
            WebElement.rightarrow.click() 
     
            id = id +1
            time.sleep(3)

        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//span[@class='view-all']/a)[2]").click()
        idd = 0
        while idd <5:
  
            arrows=By.XPATH,"//li[@class='next arrow']"
    
            WebElement.rightarroww = wait.until(EC.visibility_of_element_located(arrows))
      
            WebElement.rightarroww.click() 
     
            idd = idd +1
            time.sleep(3)
            
        
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//span[@class='view-all']/a)[3]").click()
        idx = 0
        while idx <5:
  
            arrowd=By.XPATH,"//a[contains(.,'Next >')]"
    
            WebElement.rightarrowwd = wait.until(EC.visibility_of_element_located(arrowd))
      
            WebElement.rightarrowwd.click() 
     
            idx = idx +1
            time.sleep(3)
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//span[@class='view-all']/a)[4]").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        #self.driver.find_element(By.XPATH,"(//span[@class='view-all']/a)[5]").click()'''