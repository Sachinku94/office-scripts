from utilities.Base_class import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
#@pytest.mark.usefixtures("setup")
class Test_Deep_Dives(BaseClass):
    def test_PW7(self):
        wait= WebDriverWait(self.driver,20)
        AC=ActionChains(self.driver)
        hover=By.XPATH,"//a[normalize-space()='DEEP DIVES']"
        
        try:
            
         element =  self.driver.find_elements(By.XPATH,"(//ul[@class='mega-sub-menu'])[6]/li/a")
        
        except exceptions.StaleElementReferenceException:
         
          print("")
         
        for clck in element:
            Hover=wait.until(EC.presence_of_element_located(hover))
           
            AC.move_to_element(Hover)
           
            time.sleep(2)
         
            a =clck.get_dom_attribute('href')
            
            if a.__contains__('https://www.physiciansweekly') :
            
             AC.key_down(Keys.CONTROL).click(clck).key_up(Keys.CONTROL).perform()
            
            #assert a.__contains__('https://staging.physiciansweekly.com')==False
            
            if a==None:
             continue