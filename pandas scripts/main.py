# import pandas as pd


# execelfile = r'C:\Users\Primotech\Documents\pw-linkstesting\Pw-externallinks.xlsx'
# data = pd.read_excel(execelfile)
# def replace_www_with_dev(url): 
#     return url.replace('www', 'preview')


# data['Source'] = data['Source'].apply(replace_www_with_dev)
# data.to_excel('modified_excel_file.xlsx', index=False)
# print("Modified DataFrame saved to 'modified_excel_file.xlsx'")

# print(data)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
driver=webdriver.Chrome()
a="For Additional FL (Follicular Lymphoma) News from OncWeekly – Your Front Row Seat To The Future of Cancer Care –"
print(len(a))
driver.get("https://oncweekly.com/lbc-vs-cell-blocks-in-cervical-pathology/")
time.sleep(10)
link_text=driver.find_element(By.XPATH,"//div[@id='ad-msg-article']").text
print(len(link_text))