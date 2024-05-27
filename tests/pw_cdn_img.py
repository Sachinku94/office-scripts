import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\cdn test links.xlsx'
status_link=[]

# Read the Excel file into a DataFrame
df = pd.read_excel(execelfile)
def send_url(page_url):
  
    driver=webdriver.Chrome()
    AC=ActionChains(driver)
    img_link=[]
    allsociallinks=[]
    
    driver.get("https://cdn.physiciansweekly.com/")
    # driver.find_element(By.XPATH,"//input[@type='password']").send_keys("pw@123!")
    # driver.find_element(By.XPATH,"//input[@type='submit']").click()
    driver.get(page_url)
    imglinks=driver.find_elements(By.TAG_NAME,"img")

    for imgl in imglinks:
        decode=imgl.get_attribute("decoding")
        if  decode !=None:
         img=imgl.get_attribute("src")
         img_link.append(img)
    for imgll in img_link:
        if imgll.__contains__("https://img-dev.physiciansweekly.com/"):
           status_link.append("pass")
        else:
           status_link.append("fail")   
           print(imgll)
        
    
    time.sleep(60)
    

         


# Loop through each row in the DataFrame
for index, row in df.iterrows():
    page_url = row["URL's"]
    status = row['STATUS']
    
    send_url(page_url)
    
    # Update speed_url and page_url with the respective values from the lists
    df.at[index, 'STATUS'] = status_link[index] 
    
    
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\updat_excel_file_cdnfail.xlsx'
df.to_excel(updated_execelfile, index=False)
