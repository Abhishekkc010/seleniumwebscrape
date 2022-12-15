import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe'
,options=options)

URL = 'https://pythonbasics.org'
driver.get(URL)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))                                                                                                                 
driver.find_element_by_tag_name('body').screenshot('./ss/this.png')
driver.quit()