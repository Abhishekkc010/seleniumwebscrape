from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import numpy as np
import time
import csv
import os



def get_data(driver):
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
        list.append([value,title,desc,link])
        i=i+1
        if (i==5):
            break
    return list




value = input("Enter any word for google : ")

#PATH ="C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe') 



try:
    driver.get("https://www.google.com")

    english=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"English"))
    ).click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
    )

    search.clear()

    search.send_keys(value)
    search.send_keys(Keys.RETURN)

    results = get_data(driver)

    empty=[value,np.nan,np.nan,np.nan]


    while ( len(results) != 5 ):
        results.append(empty)


    heading = ['search topic','title','description','link']
    exist=os.path.isfile('google.csv')


    with open('google.csv','a') as f:
        write =csv.writer(f)
        if not exist:
            write.writerow(heading)
        write.writerows(results)



finally:
    time.sleep(10)
    driver.quit()