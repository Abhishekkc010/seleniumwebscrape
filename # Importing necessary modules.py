# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver Chrome
driver = webdriver.Chrome()

# Target URL
driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
# To load entire webpage
time.sleep(5)

# Printing the whole body text
print(driver.find_element(By.XPATH, "/html/body").text)

# Closing the driver
driver.close()
