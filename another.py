from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe') 

driver.get('https://www.google.com/search?q=apple&sxsrf=ALiCzsaoTbRIefERGOBOuPyNBatN4l25xg%3A1670402951817&ei=h1OQY4evMayz4-EP5ICRoAM&ved=0ahUKEwjHjsz0j-f7AhWs2TgGHWRABDQQ4dUDCA8&uact=5&oq=apple&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIHCAAQsQMQQzIQCC4QxwEQ1AIQsQMQ0QMQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIHCAAQsQMQQzoHCCMQsAMQJzoKCAAQRxDWBBCwAzoSCC4QxwEQ0QMQyAMQsAMQQxgBOgwILhDIAxCwAxBDGAE6EAguEIMBEMcBELEDENEDEEM6CggAELEDEIMBEEM6EAgAEIAEEIcCELEDEIMBEBQ6BQgAELEDOgsIABCABBCxAxCDAToQCC4QsQMQgwEQxwEQ0QMQQzoNCC4QxwEQ0QMQ1AIQQzoNCC4QxwEQsQMQ0QMQQzoKCC4QxwEQ0QMQQzoECC4QQ0oECEEYAEoECEYYAFDyA1jqEmD7FGgBcAF4AIAB0wGIAfANkgEFMC43LjKYAQCgAQHIAQvAAQHaAQQIARgI&sclient=gws-wiz-serp')

driver.implicitly_wait(2)

desc=driver.find_elements(By.XPATH,'//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"] | //div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
desc_list=[]
for d in desc:
    if d.text =="":
        desc_list.append("(Not Found)")
    else:    
        desc_list.append(d.text)
print(desc_list)




#dont Touch
title=driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]//h3[@class="LC20lb MBeuO DKV0Md"]')
title_list=[]
for t in title:
    if t.text =="":
        title_list.append("(Not Found)")
    else:    
        title_list.append(t.text)
print(title_list)



#dont Touch
Link=driver.find_elements(By.XPATH, '//div[@class="TbwUpd NJjxre"]//cite')
Link_list=[]
for L in Link:
    if L.text =="":
        Link_list.append("(Not Found)")
    else:    
        Link_list.append(L.text)
print(Link_list)

this_dics={
    "desc":desc_list[:],
    "links":Link_list[:],
    "title":title_list[:]
}
print(this_dics)
driver.quit()
print(len(desc_list))
print(len(Link_list))
print(len(title_list))


new = pd.DataFrame.from_dict(this_dics)
  
new.to_csv('this.csv2')