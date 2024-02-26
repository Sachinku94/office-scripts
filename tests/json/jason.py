import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
with open('C:\\Users\\Primotech\\Documents\\url_lms.json', encoding="utf-8") as f:
    data = json.load(f)
num=0

 
driver = webdriver.Chrome()

for url in data:
 try:    
   driver.get(url["URL"])
   num=num+1
   page=driver.find_elements(By.XPATH,"//div[@id='crumbs']")
   for pa in page:
       
    if pa.is_displayed: 
        p=pa.get_attribute('href')
        print(p)
    elif pa.is_displayed==None:
        continue
        


     
       
            
 except requests.exceptions.InvalidSchema:
     ("")
       
 print(num)