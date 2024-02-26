

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time
import re
driver=webdriver.Chrome()

driver.get("https://support.google.com/")
elements=driver.find_elements(By.XPATH,"//section[@class='product-selector']//ul/li")



        
 
AC=ActionChains(driver)
wait = WebDriverWait(driver, 2)
for ele in elements:
    AC.key_down(Keys.CONTROL).click(ele).key_up(Keys.CONTROL).perform()
    


       
        
      
 


# ... (previous code)

# ... (previous code)

# ... (previous code)

handles = driver.window_handles
for i in handles:
    try:
        driver.switch_to.window(i)
        time.sleep(3)
        driver.refresh()
        modul = driver.find_element(By.XPATH, "(//li[@class='appbar-helpcenter-list__item']/a)[2]")
        if modul.is_displayed():
            modul.click()
        elif not modul.is_displayed():
            continue

        view = driver.find_element(By.XPATH, "//a[normalize-space()='View all posts']")
        view.click()
        time.sleep(3)
        thread = driver.find_element(By.XPATH, "//div[@class='thread-list']")
        Text = thread.text
        view_more = driver.find_element(By.XPATH, "//button[@class='thread-list-threads__load-more-button material2-button material2-button--hairline']")

        view_more.click()
        driver.refresh()
        thread = driver.find_elements(By.XPATH, "(//div[@class='thread-list-group'])")
        printed_texts = set()
        found_this_week = False  # Flag to track if "Updated: This week" is found

        for thr in thread:
            th = thr.text

            while not th.__contains__("Updated: This week"):
                vw = By.XPATH, "//button[@class='thread-list-threads__load-more-button material2-button material2-button--hairline']"
                WebElement.view = wait.until(EC.visibility_of_element_located(vw))
                WebElement.view.click()
                time.sleep(3)
                tv = By.XPATH, "(//div[@class='thread-list-group'])"
                tt = wait.until(EC.visibility_of_all_elements_located(tv))

                for td in tt:
                    tl = td.text

                    if "Updated: This week" in tl:
                        found_this_week = True  # Set the flag to True when "Updated: This week" is found
                        break

                if found_this_week:
                    break  # Exit the loop if "Updated: This week" is found

            if found_this_week:
                continue
            
        time.sleep(5)
        tn = By.XPATH, "//div[@class='thread-list-group']"
        tp = wait.until(EC.visibility_of_all_elements_located(tn))    
        for ty in tp:
         tz = ty.text
         if "Updated: This week" in tz:
         
          Week = By.XPATH, "//div/div/div/a[@class='thread-list-thread']"
          weekly = wait.until(EC.visibility_of_all_elements_located(Week))
          repliii = []

          for weeks in weekly:
            we = weeks.text

            for w in we:
                repliii.append(we)
                
                for text in repliii:
                  match = re.search(r'(\d+) Replies', text)
                   
                  if match:
                    reply_value = int(match.group(1))
                    if reply_value > 1 and text not in printed_texts:
                     printed_texts.add(text)
                     print(text)
                     print(reply_value)

    except NoSuchElementException:
        ()
