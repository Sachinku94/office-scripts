import pandas as pd
from selenium import webdriver
from selenium.common import exceptions


# Path to your Excel file
execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\redirection-www-physiciansweekly-com-duplicates.csv'

# Read the Excel file into a DataFrame
df = pd.read_csv(execelfile)

# Function to check URL redirection
def check_redirection(source_url, target_url):
    driver = webdriver.Chrome()
    driver.get(source_url)
    current_url = driver.current_url
    driver.quit()
    return current_url == target_url

# List to store the results
results = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    source_url = row['source']
    target_url = row['target']
    try:
     
        if check_redirection(source_url, target_url):
            results.append('Pass')
        else:
            results.append('Fail')
    
    except exceptions:
       results.append('URL not found')

# Add the results to the DataFrame
df['status'] = results

# Save the DataFrame with the results to a new Excel file
result_file = r'C:\Users\Primotech\Documents\pw-linkstesting\redirection-results.xlsx'
df.to_excel(result_file, index=False)

print("Result saved to:", result_file)
