from utilities.Base_class import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

#@pytest.mark.usefixtures("setup")
class Testspotlights(BaseClass):
    def test_PW4(self):
        wait=WebDriverWait(self.driver,20)
        self.driver.implicitly_wait(10)
        AC=ActionChains(self.driver)
        hover=self.driver.find_element(By.XPATH,"//a[normalize-space()='DEEP DIVES']")
        click=self.driver.find_elements(By.XPATH,"(//ul[@class='mega-sub-menu'])[6]/li/a")
        #Table=self.driver.find_element(By.XPATH,"(//ul[@class='mega-sub-menu'])[6]")
        #table=wait.until(EC.visibility_of_element_located(Table))
       
        for CLICK in click :
            
       
            AC.move_to_element(hover)
            time.sleep(10)
            a = CLICK.get_dom_attribute('href')
            
            
            if a.__contains__('https://www.physiciansweekly') :
            
             AC.key_down(Keys.CONTROL).click(CLICK).key_up(Keys.CONTROL).perform()
             
              
            
            #assert a.__contains__('https://staging.physiciansweekly.com')==False
            
            if a==None:
                continue
            
        time.sleep(25)
        handles =self.driver.window_handles    
        for i in handles:
                self.driver.switch_to.window(i)
                elems =self.driver.find_elements(By.XPATH,"//a[@href]")
                for elem in elems:
                 print(elem.get_attribute("href"))
                
                
                
                time.sleep(20)    
                 
        time.sleep(10)
        
        

            
        
        
            
         
        
         
         

        