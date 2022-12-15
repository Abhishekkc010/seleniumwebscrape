from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
import time
import csv
import os

def fullimage(driver):
    main_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1550,main_height)
    driver.save_screenshot(f'{save_image}\\full.png')

def smallimage(driver):
    driver.set_window_size(1550,926)
    driver_height =926

    main_height = driver.execute_script("return document.body.scrollHeight")

    searchbox = driver.find_element(By.XPATH,'//div[contains(@class,"CvDJxb")]')
    remove_size = searchbox.size
    remove_height = remove_size.get('height')

    first_remove = driver.find_element(By.XPATH,'//div[@jscontroller="HYSCof"]')
    first_remove_size = first_remove.size
    first_remove_height = first_remove_size.get('height')

    extra_remove = driver.find_element(By.XPATH,'//div[contains(@class,"appbar")]')
    extra_size = extra_remove.size
    extra_height =extra_size.get('height')

    driver.save_screenshot(f'{save_image}\\0.png')
    i = 1
    scrolled = 0
    scroll= driver_height - remove_height - first_remove_height - extra_height

    while(scrolled+scroll < main_height):
        driver.execute_script(f"window.scrollTo(0,{scrolled+scroll})")
        scrolled+= scroll
        driver.save_screenshot(f'{save_image}\\{i}.png')
        i += 1

def get_data(driver):
    v_list=[]
    i=0
    searches = driver.find_elements(By.XPATH,'//div[contains(@class,"g Ww4FFb") or contains(@jscontroller,"SC7lYd")]')
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
            desc = p.find_element(By.XPATH,'.//div[contains(@class,"VwiC3b")]').text
            desc = desc.str.replace(".*—","",regex=True)
            desc = desc.str.lstrip(' ')
        except:
            desc=np.nan
        v_list.append([value,title,desc,link])
        i=i+1
        if (i==5):
            break
    return v_list

value = input("Enter what to search : ")

PATH ="C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.headless = True
driver = webdriver.Chrome (PATH,options = options)

save_image = f"C:\\Users\\Sagun\\Desktop\\interns\\pra_selenium\\index\\image\\{value}"
file_exist = os.path.exists(save_image)
if not file_exist:
    os.mkdir(save_image)

try:

    driver.get("https://www.google.com")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"English"))
    ).click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
    )

    search.clear()

    search.send_keys(value)
    search.send_keys(Keys.RETURN)

    results = get_data(driver)
    fullimage(driver)
    smallimage(driver)

    while ( len(results) != 5 ):
        empty=[value,np.nan,np.nan,np.nan]
        results.append(empty)

    heading = ['search topic','title','description','link']

    exist=os.path.isfile('google.csv')

    if(exist):
        df=pd.DataFrame(list(results))
        df.to_csv("google.csv",mode='a',header=False,index=False)

    else:
        df=pd.DataFrame(list(results),columns = heading)
        df.to_csv("google.csv",index=False)

finally:
    driver.quit()