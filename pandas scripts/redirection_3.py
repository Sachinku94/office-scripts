import pandas as pd
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Function to check URL redirection
def check_redirection(source_url, target_url):
    driver = webdriver.Chrome()
    
    driver.get(source_url)
    current_url = driver.current_url
    
    while current_url == source_url:
        time.sleep(1)  # Adjust sleep time as needed
        current_url = driver.current_url
        if current_url == target_url:
            break
    
    driver.quit()
    return current_url

# Path to your CSV file
csv_file_path = r'C:\Users\Primotech\Documents\pw-linkstesting\scripts all\pandas scripts\new redirection.xlsx'

# Read the CSV file into a DataFrame
df = pd.read_excel(csv_file_path, header=None, names=['source', 'target'])

# Function to process each row in parallel
def process_row(row):
    source_url = row.source
    target_url = row.target
    try:
        # Check redirection
        if check_redirection(source_url, target_url):
            return 'Pass'
        else:
            return 'Fail'
    except:
        return 'Error'  # Handle exceptions such as invalid URLs or timeout errors

# Number of concurrent threads (adjust as needed)
num_threads = 20


# Process rows in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    results = list(executor.map(process_row, df.itertuples(index=False)))

# Add the results to the DataFrame
df['redirection_check'] = ''
for index, row in df.iterrows():
    source_url= row['source']
    target_url = row['target']
    df.at[index,'redirection_check'] =  results[index]

# Save the DataFrame with the results to a new CSV file
result_csv_file_path = r'C:\Users\Primotech\Documents\pw-linkstesting\scripts all\pandas scripts\redirection_01results.xlsx'
df.to_csv(result_csv_file_path, index=False)

print("Result saved to:", result_csv_file_path)