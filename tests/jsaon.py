import pandas as pd
from pandas import json_normalize

# Load the JSON file
import json
with open('C:\\Users\\Primotech\\Screenshots\\Link.json', 'r') as file:
 data = json.load(file)

# Normalize JSON data
df = json_normalize(data)

# Save to Excel file
df.to_excel('C:\\Users\\Primotech\\Screenshots\\Newd.xlsx', index=False, engine='openpyxl')

print("JSON data has been successfully converted to Excel file.")
