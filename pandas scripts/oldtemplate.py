import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\pw test links_fails.xlsx'
status_link = []
result_link = []

# Read the Excel file into a DataFrame
df = pd.read_excel(execelfile)

def send_url(page_url):
    driver = webdriver.Chrome()
    AC = ActionChains(driver)
    img_link = []
    allsociallinks = []

    try:
     try:
     
      driver.get(page_url)
      imglinks = driver.find_element(By.XPATH, "//div[@class='textwidget']//form[@class='subscription_form']")

      if imglinks.is_displayed:
        current_url=driver.current_url
    
    
        status_link.append("fail")
        result_link.append(current_url)
      elif not imglinks.is_displayed:
           status_link.append("pass")
     except NoSuchElementException:
        status_link.append("pass")
    except TimeoutException:
        status_link.append("pass")

    
    driver.quit()

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    page_url = row["URL's"]
    status = row['STATUS']

    send_url(page_url)

    # Update status_link with the respective values from the lists
    df.at[index, 'STATUS'] = status_link[index]

# Create a new DataFrame for failed links
failed_links_df = pd.DataFrame(result_link, columns=['Failed Links'])

# Save the updated DataFrame and the failed links DataFrame to a new Excel file
with pd.ExcelWriter(r'C:\Users\Primotech\Documents\pw-linkstesting\updated_excel_file_oldtemplate.xlsx') as writer:
    df.to_excel(writer, sheet_name='Main Data', index=False)
    failed_links_df.to_excel(writer, sheet_name='Failed Links', index=False)
