import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\cdn test links.xlsx'
status_link = []
result_link = []

# Read the Excel file into a DataFrame
df = pd.read_excel(execelfile)

def send_url(page_url):
    driver = webdriver.Chrome()
    AC = ActionChains(driver)
    img_link = []
    allsociallinks = []

    driver.get("https://cdn.physiciansweekly.com/")
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

    time.sleep(60)
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
with pd.ExcelWriter(r'C:\Users\Primotech\Documents\pw-linkstesting\updated_excel_file_cdnfail.xlsx') as writer:
    df.to_excel(writer, sheet_name='Main Data', index=False)
    failed_links_df.to_excel(writer, sheet_name='Failed Links', index=False)
