from utilities.Base_class import BaseClass

from selenium.webdriver.common.by import By
import time
#@pytest.mark.usefixtures("setup")
class TestHomepage2(BaseClass):
    def test_PW2(self):
        self.driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[1]").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[2]").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[3]").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[4]").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[5]").click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='view-more']/a)[6]").click()