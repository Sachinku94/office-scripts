import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import concurrent.futures
import time
import requests
from bs4 import BeautifulSoup



# Read the Excel file into a DataFrame
execelfile = r'C:\\Users\\Primotech\\Screenshots\\File1.xlsx'
df = pd.read_excel(execelfile)
result_link=[]

# Define the send_url function
def send_url(page_url):
    driver = webdriver.Chrome()
    AC = ActionChains(driver)
    img_link = []
    status_link = []
    
    try:
        driver.get(page_url)
        imglinks = driver.find_elements(By.TAG_NAME, "img")

        for imgl in imglinks:
            decode = imgl.get_attribute("decoding")
            if decode is not None:
                img = imgl.get_attribute("src")
                img_link.append(img)

        for imgll in img_link:
            if "https://img-dev.physiciansweekly.com/" in imgll:
                status_link.append("pass")
            else:
                status_link.append("fail")
                result_link.append(imgll)


        if "fail" in status_link:
            return "fail"
        else:
            return "pass"
    except Exception as e:
        return "fail"
    finally:
        driver.quit()

# List to store status for each URL
status_results = []

# Use ThreadPoolExecutor to run send_url concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(send_url, row["URL's"]): index for index, row in df.iterrows()}
    for future in concurrent.futures.as_completed(futures):
        index = futures[future]
        try:
            status = future.result()
        except Exception as e:
            status = "fail"
        status_results.append((index, status))

# Update the DataFrame with the results
for index, status in status_results:
    df.at[index, 'STATUS'] = status

# Create a new DataFrame for failed links
failed_links_df = pd.DataFrame(result_link, columns=['Failed Links'])

# Save the updated DataFrame and the failed links DataFrame to a new Excel file
with pd.ExcelWriter(r'C:\\Users\\Primotech\\Screenshots\\updated_excel_file_cdnfail_6.xlsx') as writer:
    df.to_excel(writer, sheet_name='Main Data', index=False)
    failed_links_df.to_excel(writer, sheet_name='Failed Links', index=False)
