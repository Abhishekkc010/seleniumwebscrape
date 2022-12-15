import code


list1=["aa","gg","ff","bb"]
list2=["gg","ff","hh"]



list3=[c for c in list1 if c in list2] 
print (list3)


list4 = set(list1).intersection(list2)
print(list4)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys   ##gives acces to certain keys
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
import argparse
import numpy as np 
import os
from selenium.webdriver.chrome.options import Options


##get titles
def get_title(element):
    titles = []
    for m in element:
        try:
            titles.append(m.find_element(By.XPATH,'.//div[@class="yuRUbf"]//h3 | .//h3' ).text)
        except:
            titles.append(np.nan)
    return titles


##get links
def get_link(element):
    links = []
    for m in element:
        try:
            links.append((m.find_element(By.XPATH,'.//div[@class="yuRUbf"]//a | .//a').get_attribute('href')))
        except:
            links.append(np.nan)
    return links


##get descriptions
def get_desc(element):
    desc = []
    for m in element:
        try:
            desc.append(m.find_element(By.XPATH,'.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"] | .//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"] |  .//div[@class="zz3gNc"]').text)
        except:
            desc.append(np.nan)      
    return desc 


##dont actually need to create this function
def get_search_topic(element,searchKey):
    search_topic = []
    for m in element:
        search_topic.append(searchKey)
    return search_topic


#main function
def google_crawler(searchKey,search_count):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.google.com")
    # driver.manage().window().maximize()
    driver.set_window_size(1550, 926)
    
    language=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/a')
    if language != 'English':
        language.send_keys(Keys.RETURN)
   
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//div/input[1]'))
        )
        element.send_keys(searchKey)
        element.send_keys(Keys.RETURN)
       
        entire_body = driver.find_element(By.TAG_NAME,'html')
        pageHeight = driver.execute_script("return document.body.scrollHeight")
       
        base_directory = './Screenshot/'
        try:
            os.mkdir(base_directory)
        except:
            pass
        image_dir = f'{searchKey}'
        final_path = os.path.join(base_directory,image_dir)

        i=0
        try:
            os.mkdir(final_path)
        except:
            pass 

        totalScrolledHeight = 0 
        # print(totalScrolledHeight,pageHeight)
        while True:
            driver.save_screenshot(f'./{final_path}/{i}.png')
            entire_body.send_keys(Keys.PAGE_DOWN)
            
            totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
            i += 1 
            # print(totalScrolledHeight,pageHeight)   
            if(totalScrolledHeight+1 > pageHeight):
                break
        
        main=driver.find_elements(By.XPATH,'//div[@jscontroller="SC7lYd"] | //div[@class="usJj9c"] ')
        driver.set_window_size(1920, pageHeight)
        driver.save_screenshot(f"{final_path}/full_page.png")
        #function calls
        links = get_link(main)
        desc = get_desc(main)
        titles = get_title(main)
        search_key = get_search_topic(main, searchKey)
        csv_dir = './CSV'
        try:
            os.mkdir(csv_dir)
        except:
            pass 


        #creating csv
        if search_count != 0:
            df = pd.DataFrame(list(zip(search_key, titles,links,desc,)))
            df.to_csv(f'./{csv_dir}/{args.dfName}.csv',mode='a',header=False,index=False)
        else:
            df = pd.DataFrame(list(zip(search_key, titles,links,desc)),columns=['SearchKey','Title','Link','Desc'])
            df.to_csv(f'./{csv_dir}/{args.dfName}.csv',index=False)
    except:
        driver.quit()
    finally:
        driver.quit()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Search for the item in gogogle')
    parser.add_argument('-s','--searchKey',nargs='+',default=[], type=list,help='Type the key you want to search')
    parser.add_argument('-d','--dfName',default='result', type=str,help='Type the key you want to search')
    args = parser.parse_args()
    i=0
    for search_item in args.searchKey: 
       item =  ''.join(search_item)
       google_crawler(item, i )
       i += 1
    # google_crawler('Apple',0)

