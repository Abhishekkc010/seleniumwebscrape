from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe')


driver.get('https://www.google.com/search?q=apple&rlz=1C1GCEB_enNP875NP875&oq=apple&aqs=chrome.0.69i59j35i39j0i67i433j46i67i199i433i465j0i67j69i60l2j69i61.1124j0j7&sourceid=chrome&ie=UTF-8')

title=driver.find_element_by_xpath("//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]").text

title_list=[]
title_list.append(title)
#print("Title",title_list)

"\n"

desc=driver.find_element_by_xpath('//body[1]/div[7]/div[1]/div[11]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]').text

desc_list=[]
desc_list.append(desc)
#print("Description",desc_list)

"\n"
links=driver.find_element_by_xpath("//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").text

link_list=[]
link_list.append(links)
#print("LINk",link_list )

this_dics={
    "desc":desc_list,
    "links":link_list,
    "title":title_list
}

print("Ok cool",this_dics)

driver.quit()