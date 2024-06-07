import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\pw test links_fails.xlsx'
status_link = []
result_link = []

# Read the Excel file into a DataFrame
df = pd.read_excel(execelfile)

# Initialize a counter for the number of URLs tested
url_count = 0

def send_url(page_url):
    global url_count  # Access the global counter variable
    driver = webdriver.Chrome()
    AC = ActionChains(driver)
    
    try:
        driver.get(page_url)
        imglinks = driver.find_element(By.XPATH, "//div[@class='textwidget']//form[@class='subscription_form']")

        if imglinks.is_displayed:
            current_url = driver.current_url
            status_link.append("fail")
            result_link.append(current_url)
        else:
            status_link.append("pass")
    except NoSuchElementException:
        status_link.append("pass")
    except TimeoutException:
        status_link.append("pass")
    finally:
        url_count += 1  # Increment the counter
        driver.quit()

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    page_url = row["URL's"]

    send_url(page_url)

    # Update status_link with the respective values from the lists
    df.at[index, 'STATUS'] = status_link[index]

    # Save progress to the Excel file after processing each URL
    with pd.ExcelWriter(r'C:\Users\Primotech\Documents\pw-linkstesting\updated_excel_file_oldtemplate.xlsx') as writer:
        df.to_excel(writer, sheet_name='Main Data', index=False)
        failed_links_df = pd.DataFrame(result_link, columns=['Failed Links'])
        failed_links_df.to_excel(writer, sheet_name='Failed Links', index=False)

# Print the total count of tested URLs
print(f"Total URLs tested: {url_count}")
