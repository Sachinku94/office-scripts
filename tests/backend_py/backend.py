from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome


driver.get("https://www.physiciansweekly.com/pw-adm-logs/")
driver.find_element(By.XPATH,"//input[@id='user_login']").send_keys("sachinprimo")
driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("LMp4fs37sXAXNb2a^uZr^ltp")
driver.find_element(By.XPATH,"//input[@id='wp-submit']").click()
time.sleep(30)
Achains = AC(driver)
Achains.key_down(Keys.CONTROL).click("https://www.physiciansweekly.com/wp-admin/edit.php?s&post_status=all&post_type=post&action=-1&m=0&cat=6984&post_format&author_name&wallboard_articles&author_admin_filter=0&filter_action=Filter&paged=1&action2=-1").key_up(Keys.CONTROL).perform()


