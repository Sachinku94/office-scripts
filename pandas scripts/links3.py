import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Path to the Excel file
execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\pwtest.xlsx'

# Read the Excel file
df = pd.read_excel(execelfile)

# Function to extract hrefs from a webpage
'''def extract_hrefs(url):
    driver = webdriver.Chrome() 
    driver.get(url)
    
    # Example: If authentication is required
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys('pw@123!')
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    
    links = driver.find_elements(By.TAG_NAME, 'a')
    hrefs = [link.get_attribute('href') for link in links]
    
    driver.quit()  # Close the WebDriver after extraction
    return hrefs'''

# Function to handle actions based on devops status
def handle_devops_status(source_url,status, destination_url):
    driver = webdriver.Chrome() 
    if status.startswith('Destination URL was 404') or status.startswith('Destination URL was https and 403'):
        driver.get(source_url)
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys('pw@123!')
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        links = driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
         http=[]
         href = link.get_attribute('href')
         http.append(href)
         if destination_url in http:
            link.send_keys(Keys.CONTROL + Keys.RETURN)
            
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            window1_url = driver.current_url
            
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            
            

# Add a new column 'Status' to store pass/fail status
df['Status'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    source_url = row['Source']
    devops_status = row['DevOpsStatus']
    destination_url = row['Destination']

    # Extract hrefs from the source_url
    #hrefs = extract_hrefs(source_url)

    # Handle actions based on devops status and destination URL
    status = handle_devops_status(source_url,devops_status, destination_url)
    df.at[index, 'Status'] = status

# Save the updated DataFrame with status column to a new Excel file
updated_execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\updated_excel_file.xlsx'
df.to_excel(updated_execelfile, index=False)