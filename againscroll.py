from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
import os

driver = webdriver.Chrome('C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe')

driver.get('https://www.amazon.com/')

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
""" time.sleep(3)
height = driver.execute_script("return document.body.scrollHeight")
for scrol in range(100,height,75):
    driver.execute_script(f"window.scrollTo(0,{scrol})")
    time.sleep(0.1) """


save_image = f"C:/Users/Dell/Desktop/Selenium/ss/the"

main_height = driver.execute_script("return document.body.scrollHeight")

driver.set_window_size(1550,926)
driver_height =926
driver.save_screenshot(f'{save_image}\\0.png')
i = 1
scrolled = 0
scroll= driver_height

while(scrolled+scroll < main_height):
        driver.execute_script(f"window.scrollTo(0,{scrolled+scroll})")
        scrolled+= scroll
        driver.save_screenshot(f'{save_image}/{i}.png')
        i += 1

file_exist = os.path.exists(save_image)
if not file_exist:
    os.mkdir(save_image)

driver.quit()