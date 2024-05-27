import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\cdn links.xlsx'
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
    imglinks=driver.find_elements(By.XPATH,"//div[@class='post-media']/a")

    for imgl in imglinks:
        imgl.get_attribute("href")
        img_link.append(imgl)
    for imgll in img_link:
        driver.execute_script("window.open(arguments[0])", imgll)
        
    
    time.sleep(60)
    handles =driver.window_handles

    for windows in handles:
        driver.switch_to.window(windows)
        alllinks=driver.current_url
        allsociallinks.append(alllinks)
    for social in allsociallinks:
            response = requests.get(social)


            status_code = response.status_code
            print("verfying any broken links")
            if status_code == 404 :
                 status_link.append("fail")
            if status_code != 404 :
                 status_link.append("pass")

            
df['Status'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    page_url = row["URL's"]
    status = row['STATUS']
    
    send_url(page_url)
    
    # Update speed_url and page_url with the respective values from the lists
    df.at[index, 'STATUS'] = status_link[index] 
    
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\updat_excel_file_cdn.xlsx'
df.to_excel(updated_execelfile, index=False)