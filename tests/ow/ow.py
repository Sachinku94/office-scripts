import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time


execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\owp.xlsx'


df = pd.read_excel(execelfile)

list_1=[]
list_2=[]
list_3=[]
list_4=[]

def send_url(page_url):
  driver= webdriver.Chrome()
  wait=WebDriverWait(driver,100)
  
  driver.get("https://pagespeed.web.dev/")
  time.sleep(5)
  driver.find_element(By.XPATH,"//input[@type='text']").send_keys(page_url)
  time.sleep(2)
  driver.find_element(By.XPATH,"(//span[@jsname='V67aGc'])[5]").click()
  driver.maximize_window()
  driver.refresh()
  try:
   error=driver.find_element(By.XPATH,"(//div[@class='lh-gauge__percentage lh-gauge--error'])[1]")
   if error.is_displayed:
    driver.find_element(By.XPATH,"(//span[@jsname='V67aGc'])[5]").click()
    
  except NoSuchElementException:
   
  
   
  
    text=By.CSS_SELECTOR,"text.lh-exp-gauge__percentage"
    tp=wait.until(EC.presence_of_all_elements_located(text)) 
  
    for tn in tp:
     tl=tn.text
     if tl.strip():
      
  
   
    
     
      list_1.append(tl)
     else:
      list_1.append('na')
       
  
    
      print(list_1)
    
      time.sleep(10)
      
     CT=driver.current_url
     if CT==None:
      list_2.append("na")
     else:
       
       list_2.append(CT)
      
  
     driver.find_element(By.CSS_SELECTOR,"#desktop_tab").click()
  
     time.sleep(10)
  
     try:
      error=driver.find_element(By.XPATH,"(//div[@class='lh-gauge__percentage lh-gauge--error'])[1]")
      if error.is__displayed__():
       list_1.append('na')
    
     except NoSuchElementException:
    
  
    
      text=By.CSS_SELECTOR,"text.lh-exp-gauge__percentage"
      tq=wait.until(EC.presence_of_all_elements_located(text))
      for ts in tq:
  
   
       td=ts.text
       if td.strip():
    

        list_3.append(td)
       else :
        list_3.append("na")
        print(list_3)
        CU=driver.current_url
  
        if CU == None:
          list_4.append("na")
        else:
          
  
         list_4.append(CU)
        
  
  
  
  
        print(list_4)

df['Status'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    page_url = row['Page URL']
    speed_url = row['Speed URL']
    speed = row['Speed']  
    send_url(page_url)
    
    # Update speed_url and page_url with the respective values from the lists
    df.at[index, 'Speed URL'] =  list_2[index] + ' ' + list_4[index]
    df.at[index, 'Speed'] = 'mobile' + ' ' +list_1[index] + 'desktop' + ' ' + list_3[index]
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\update_excel_file.xlsx'
df.to_excel(updated_execelfile, index=False)    