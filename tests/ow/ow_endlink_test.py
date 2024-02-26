import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains as AChains
from selenium.webdriver.common.keys import Keys
import time
import requests
execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\links_owend.xlsx'

df = pd.read_excel(execelfile)
list_1=[]
list_2=[]
list_3=[]
list_4=[]
def end_links():
   
  driver=webdriver.Chrome()
  AC=AChains(driver)
  wait=WebDriverWait(driver,20)
  driver.get("https://oncweekly.com/?lkjdjfa")
  time.sleep(10)
  es=driver.find_element(By.XPATH,"(//h2[@class='entry-title'])[10]")
  AC.key_down(Keys.CONTROL).click(es).key_up(Keys.CONTROL).perform()
 
  ea=driver.find_element(By.XPATH,"(//div[@class='el-isotope-item'])[1]/a")
  AC.key_down(Keys.CONTROL).click(ea).key_up(Keys.CONTROL).perform()
  
  time.sleep(10)
  LInks=driver.find_elements(By.XPATH,"//h4[@class='meeting-view-header']/a")
  for link in LInks:
    AC.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    

  
  driver.get("https://oncweekly.com/?lkjdjfa") 
  time.sleep(10) 
  Links_1=driver.find_elements(By.XPATH,"(//div[@class='el-dbe-blog-extra block_extended'])[1]/article/div/a") 
  for lin in Links_1:
    AC.key_down(Keys.CONTROL).click(lin).key_up(Keys.CONTROL).perform()
    
    
  
 
  handles=driver.window_handles
    
  for windows in handles:
     
    driver.switch_to(windows)
  try: 
     link_text=driver.find_element(By.XPATH,"//div[@id='ad-msg-article']").text
     if len(link_text)==129:
         list_1.append ('fail')
     else:
         list_1.append ('pass') 
     current_url=driver.current_url
     list_4.append(current_url)
     A=driver.find_element(By.XPATH,"//span[@id='parent']")
     href=A.get_attribute('href')
     if href == None:
         list_2.append('fail')
     else:
         list_2.append('pass')
     driver.execute_script("window.scrollTo(0, 2700)")
     screenshot_path = "C:/Users/Primotech/Pictures/endlinksow"
     driver.save_screenshot(screenshot_path)
     
     driver.get("https://app.prntscr.com/en/index.html")


     time.sleep(2)


     


     


     upload_url = "https://prnt.sc/upload.php"
     files = {'image': open(screenshot_path, 'rb')}
     response = requests.post(upload_url, files=files)


     screenshot_url = response.text.split('"')[3]


     print("Screenshot URL:", screenshot_url)
     list_3.append(screenshot_url)
  except NoSuchElementException:
      print(list_2)
df['Status'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    Screenshot_Recordings = row["Screenshot/Recordings"]
    status_1 = row['STATUS_1']
    status_2 =row['STATUS_2']
    Urls=row["URL's"]
    end_links()
    
    
    # Update speed_url and page_url with the respective values from the lists
    df.at[index, 'STATUS_1'] =  list_1[index] 
    df.at[index, 'STATUS_2'] = list_2[index]
    df.at[index, 'Screenshot/Recordings'] =list_3[index]
    df.at[index, "URL's"] = list_4[index]
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\updat_excel_file.xlsx'
df.to_excel(updated_execelfile, index=False)     