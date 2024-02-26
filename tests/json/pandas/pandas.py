import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\ow feed.xlsx'

df = pd.read_excel(execelfile)

list_1=[]

def send_url(page_url):
  driver= webdriver.Chrome()
  driver.get(page_url)
  items=driver.find_element(By.TAG_NAME,"item")
  if items:
      list_1.append("Data Available")
  else:
      list_1.append("empty")


df['Status'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    page_url = row["URL's"]
    status = row['STATUS']
    
    send_url(page_url)
    
    # Update speed_url and page_url with the respective values from the lists
    df.at[index, 'STATUS'] =  list_1[index] 
    
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\updat_excel_file.xlsx'
df.to_excel(updated_execelfile, index=False)