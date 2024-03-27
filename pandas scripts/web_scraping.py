from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.physiciansweekly.com/category/allergy-immunology/")

# Wait for the page to fully load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

# Extract the HTML content of the webpage
html_content = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find specific CSS rules or elements
# For example, you can find all <link> tags with rel="stylesheet" to get external CSS files
css_links = soup.find_all("link", rel="stylesheet")

# You can also find inline CSS styles within <style> tags
inline_styles = soup.find_all("style")

# Print or process the CSS links and inline styles as needed
for link in css_links:
    print("External CSS Link:", link["href"])