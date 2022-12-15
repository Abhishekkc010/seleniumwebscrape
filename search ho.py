from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.headless=True

driver = webdriver.Chrome('C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe',options=options)
URL='https://www.tutorialspoint.com/take-screenshot-of-full-page-with-selenium-python-with-chromedriver'

driver.get(URL)
def full():
    length = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1552,length)
    driver.save_screenshot("pp.png")
driver.quit()
