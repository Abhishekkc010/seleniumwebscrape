from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe') 

driver.get('https://www.google.com/search?q=amazon&rlz=1C1GCEB_enNP875NP875&biw=1536&bih=431&sxsrf=ALiCzsaM83EX1Kbm7f6MCjmao8tmQhKQ-w%3A1670391889539&ei=USiQY7rEILmuseMPwbKU2A4&ved=0ahUKEwj6sNjZ5ub7AhU5V2wGHUEZBesQ4dUDCA8&uact=5&oq=amazon&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR0oECEEYAEoECEYYAFD5A1j5A2DvBWgAcAJ4AIABAIgBAJIBAJgBAKABAcgBCMABAQ&sclient=gws-wiz-serp')

driver.implicitly_wait(2)


desc=driver.find_elements(By.XPATH,'//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"] | //div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
desc_list=[]
for d in desc:
    if d.text =="":
        desc_list.append("(Not Found)")
    else:    
        desc_list.append(d.text)
print(desc_list)

""" title=driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]//h3[@class="LC20lb MBeuO DKV0Md"]')
title_list=[]
for t in title:
    if t.text =="":
        title_list.append("(Not Found)")
    else:    
        title_list.append(t.text)
print(title_list)
 """

this_dics={
    "desc":desc_list[:],
    #"links":Link_list[:],
    #"title":title_list[:]
}

print(len(desc_list))
driver.quit()

#new = pd.DataFrame.from_dict(this_dics)
  
#new.to_csv('this.csv')