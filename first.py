from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe') 

driver.get('https://www.google.com/search?q=apple&rlz=1C1GCEB_enNP875NP875&oq=apple&aqs=chrome.0.69i59j35i39j0i67i433j46i67i199i433i465j0i67j69i60l2j69i61.1124j0j7&sourceid=chrome&ie=UTF-8')

title=driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]//h3[@class="LC20lb MBeuO DKV0Md"]')
title_list=[]
for t in title:
    if t.text !="":
        title_list.append(t.text)
print(title_list)



desc=driver.find_elements(By.XPATH,'//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]'and'//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"]')
#desc=driver.find_elements(By.XPATH,'')
desc_list=[]
for d in desc:
    desc_list.append(d.text)
print(desc_list)

driver.quit()