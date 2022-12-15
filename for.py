
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe'
,options=options)
import numpy  as np
import os
import csv

URL=("https://www.sastodeal.com/books/genre.html")
driver.get(URL) 
time.sleep(5)
def full():
    length = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1552,length)
    driver.save_screenshot("./ss/thissasto2.png")
    driver.quit
full()

list=[]
i=0
searches = driver.find_elements(By.XPATH,'//li[@class="item product product-item"]')
for p in searches:
        try:
            title=p.find_element(By.XPATH,'.//div[@class="product details product-item-details"]//a[@class="product-item-link"]').text
        except:
            title=np.nan
        try:
            price=p.find_element(By.XPATH,'.//div[@class="product details product-item-details"]//span[@class="price"]').text  
        except:
            price=np.nan
        list.append([title,price])
        

print(list)

all=[]

for books in list:
    title=str(books[0])
    price=int(books[1].replace('रू','').replace(',',''))
    all.append([title,price])

print(all)
#maximum=max(price_List(price))
#minimum=min(price_List(price))
#print(maximum)
#print(minimum)


heading = ['Title','Price']
exist=os.path.isfile('Filesasto3.csv')


with open('Filesasto3.csv','a',encoding="utf8") as f:
        write =csv.writer(f)
        if not exist:
            write.writerow(heading)
        write.writerows(all)
        



driver.quit()

