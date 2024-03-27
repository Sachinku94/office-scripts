import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Path to the Excel file
execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\PW Wallboard.xlsx'

# Read the Excel file
ttle=[]
stts=[]
cate=[]
df = pd.read_excel(execelfile)
def rssfeed(eid_s,  a1):
    driver = webdriver.Chrome()
    ei=str(eid_s)
    driver.get("https://www.physiciansweekly.com/custom-tag-rss-feed/?category_slug="+ei)
    time.sleep(10)
    Title=driver.find_elements(By.TAG_NAME,"title")
    category=driver.find_elements(By.TAG_NAME,"category")
    admin=driver.find_elements(By.TAG_NAME,"dc:creator")
    for ttl in Title:
        tt=ttl.text
        ttle.append(tt)
    print(ttle)
    if a1==ttle:
        print("pass")
        
    else:
        print("fail")
    print(a1)
    for cat in category:
        
        ca=cat.text
        
        if ca.__contains__("Wallboard"):
            print("pass")
        else:
         print("not")
        print(ca)
    for ad in admin:
        ade=ad.text
        if ade.__contains__("Physician's Weekly Admin"):
             cate.append('verified')
        else:
            cate.append("not")
        print(ade)
    print(cate)                
# Add a new column 'Status' to store pass/fail status
df['RSS Feed Status'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    eid_s=row['Eids']
    
    a1= row["A1"]
    # Handle actions based on devops status and destination URL
    rssfeed(eid_s,  a1) 
    df.at[index, 'RSS Feed Status'] =  cate[index] 
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\updatedwalbord_excel_file.xlsx'
df.to_excel(updated_execelfile, index=False)