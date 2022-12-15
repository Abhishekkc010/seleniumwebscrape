from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe')
driver.get("https://www.google.com/") 
#driver.implicitly_wait(5) 

driver.find_element_by_name("q").send_keys("javapoint")  
#click on the Google search button  
driver.find_element_by_xpath('//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]').click()
print(driver.title)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Javatpoint: Tutorials List"))
    )
    element.click()
    driver.back()
    #driver.execute_script("window.history.go(-1)")
    
finally:
    print(driver.title)
    driver.quit()

""" try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium Tutorial"))
    )
    element.click()
    
finally:
    driver.quit() """






