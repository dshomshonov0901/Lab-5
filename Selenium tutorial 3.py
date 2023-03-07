#!/usr/bin/env python
# coding: utf-8

# In[8]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service(r"C:\Users\Daniella\Favorites\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://techwithtim.net/")
link = driver.find_element(By.LINK_TEXT, "Python Programming")# finds link on webpage that has text python programming
link.click()#clicks on this link

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"
))) # wait up to 10 seconds for the driver to find the element 
    element.click()
    

    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sow-button-19310003"))) # wait up to 10 seconds for the driver to find the element this time using ID because its in a href 
    element.click()
    
    driver.back()#goes back to the previous page(we do it three times to go all the way to home page)
    driver.back()
    driver.back()
    driver.forward()#goes forward one page
    driver.forward()
except:
    driver.quit()
    




# In[ ]:




