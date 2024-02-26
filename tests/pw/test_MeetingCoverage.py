from utilities.Base_class import BaseClass

from selenium.webdriver.common.by import By
import time
#@pytest.mark.usefixtures("setup")
class TestMeetingCoverage(BaseClass):
    def test_PW3(self):
        self.driver.find_element(By.XPATH,"(//a[@class='mega-menu-link'])[24]").click()
        time.sleep(3)
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
        
            a =link.get_dom_attribute('href')
            
            if a is None:
                continue
            
            if a.__contains__('https://staging.physiciansweekly.com') :
                
                print(a)
            
            
           
            #@assert a.__contains__('https://staging.physiciansweekly.com')==False
            
            
            
            
            
        '''self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[1]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        
    
           
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[2]").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[3]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[4]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[5]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[6]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[7]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[8]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[9]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"(//a[@class='view-btnmre'])[10]").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[class='small-button smallblue']").click()
        self.driver.back()'''
        self.driver.close()