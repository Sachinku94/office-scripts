from utilities.Base_class import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class TestFooter(BaseClass):
    def test_PW6(self):
        self.driver.implicitly_wait(10)
        AC=ActionChains(self.driver)
        Footers=self.driver.find_elements(By.XPATH,"//div[@id='ft-first-row']/div/div/div/p/a")
        for Footer in Footers:
            
            a = Footer.get_dom_attribute('href')
            
            
            if a.__contains__('https://www.physiciansweekly') :
            
             AC.key_down(Keys.CONTROL).click(Footer).key_up(Keys.CONTROL).perform()
                 
             time.sleep(5)
             
             
            assert a.__contains__('https://staging.physiciansweekly.com')==False
            
            if a==None:
                continue
            