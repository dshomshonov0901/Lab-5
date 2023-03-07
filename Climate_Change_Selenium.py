#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium Chrome driver
driver = webdriver.Chrome()
PATH = Service(r"C:\Users\Daniella\Favorites\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# Open the data.gov website
driver.get("https://data.gov/")

# Find the "Data" button and click it
data_button = driver.find_element(By.LINK_TEXT, "DATA")
data_button.click()

# Find the search bar and type in "climate change"
search_bar = driver.find_element(By.ID, "search-header")
search_bar.send_keys("climate change")
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load

# Get the list of search result items
result_items = driver.find_elements(By.CLASS_NAME, "dataset-item")

# Create a CSV file to store the results
with open("climate_change_results.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Description"])
    
    # Loop through the search result items and scrape the titles and descriptions
    for item in result_items:
        title = item.find_element(By.TAG_NAME, 'a').text
        description = item.find_element(By.CLASS_NAME, 'notes').text
        writer.writerow([title, description])

# Close the browser
driver.quit()


# In[ ]:




