from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import csv
import os



driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe')
 

what=input("enter what ")
driver.implicitly_wait(5) 
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys(what)  
    #click on the Google search button  
driver.find_element_by_xpath('//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]').click()
print(driver.title)

searches = driver.find_elements(By.XPATH,'//div[@class="g Ww4FFb vt6azd tF2Cxc" or @jscontroller="SC7lYd"]')
list=[]
i=0
searches = driver.find_elements(By.XPATH,'//div[@class="g Ww4FFb vt6azd tF2Cxc" or @jscontroller="SC7lYd"]')
for p in searches:
        try:
            title=p.find_element(By.XPATH,'.//h3[@class="LC20lb MBeuO DKV0Md"]').text

        except:
            title=np.nan
        try:
            link=p.find_element(By.XPATH,'.//h3[@class="LC20lb MBeuO DKV0Md"]//parent::a').get_attribute('href')
        except:
            link=np.nan
        try:
            desc=p.find_element(By.XPATH,'.//div[contains(@class,"VwiC3b")]').text
        except:
            desc=np.nan
        list.append([what,title,desc,link])
        i=i+1
        if (i==5):
            break

print(list)

heading = ['search topic','title','description','link']
exist=os.path.isfile('File2.csv')


with open('File2.csv','a',encoding="utf8") as f:
        write =csv.writer(f)
        if not exist:
            write.writerow(heading)
        write.writerows(list)




driver.quit()

""" heading = ['search topic','title','description','link']
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(heading)
    writer.writerows(list)

 """


 

""" 
heading = ['search topic','title','description','link']
df = pd.DataFrame(list)
df.to_csv('filename.csv', index=False) """

""" this_dics={
    "list":list[:]
}
print(this_dics)
print(len(list))

new = pd.DataFrame.from_dict(this_dics)
  
new.to_csv('this2.csv')
header = ['search topic','title','description','link'] """









""" 
Link_list=[]

for l  in all:
    Link=driver.find_elements(By.XPATH, '//div[@class="TbwUpd NJjxre"]//cite')

    for L in Link:
        if L.text =="":
            Link_list.append("(Not Found)")
        else:    
            Link_list.append(L.text)
print(Link_list)


desc_list=[]
for a in all:
    desc=driver.find_elements(By.XPATH,'//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"] | //div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
    for d in desc:
        if d.text =="":
            desc_list.append("(Not Found)")
        else:    
            desc_list.append(d.text)
print(desc_list)
print(len(desc_list)) """