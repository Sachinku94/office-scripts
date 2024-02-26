from utilities.Base_class import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.common import exceptions
class Testspecialties(BaseClass):        
    def test_PW5(self):
        
        wait= WebDriverWait(self.driver,20)
        #self.driver.implicitly_wait(10)
        AC=ActionChains(self.driver)
        hov=By.XPATH,"(//a[@class='mega-menu-link'])[1]"
        
        #Hover=wait.until(EC.presence_of_element_located(hov))
       # Click_S=self.driver.find_elements(By.XPATH,"(//ul[@class='mega-sub-menu'])[1]/li/ul/li/ul/li/a")
        
        try:
            
         element =  self.driver.find_elements(By.XPATH,"(//ul[@class='mega-sub-menu'])[1]/li/ul/li/ul/li/a")
        
        except exceptions.StaleElementReferenceException:
         # Handle the exception gracefully
          print("")
         #  WebElement.rightarrow = wait.until(EC.visibility_of_any_elements_located(Click_S))
        for clck in element:
            Hover=wait.until(EC.presence_of_element_located(hov))
           
            AC.move_to_element(Hover)
           
            time.sleep(2)
         
            a =clck.get_dom_attribute('href')
            
            if a.__contains__('https://www.physiciansweekly') :
            
             AC.key_down(Keys.CONTROL).click(clck).key_up(Keys.CONTROL).perform()
            
            #assert a.__contains__('https://staging.physiciansweekly.com')==False
            
            if a==None:
             continue
         
        time.sleep(50)
        handles =self.driver.window_handles    
        for i in handles:
                self.driver.switch_to.window(i)
                elems =self.driver.find_elements(By.XPATH,"//a[@href]")
                for elem in elems:
                    el=elem.get_attribute("href")
                    print(el.__contains__('https://staging.physiciansweekly'))
                img = self.driver.find_elements(By.XPATH,"//img")
                for im in img:
                    emg=im.get_attribute("src")
        
                
                    print(emg.__contains__('https://staging.physiciansweekly'))
                
                
                
                time.sleep(20)
              