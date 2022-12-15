from selenium import webdriver


driver = webdriver.Chrome(executable_path='C:\\Users\Dell\Desktop\Growbydata\chromedriver.exe')

#driver.get("https://www.google.com")
driver.get("https://www.seleniumeasy.com/")
#driver.maximize_window()
print(driver.title)
my_element = driver.find_element_by_class_name('btn-grey')

driver.implicitly_wait(5)
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. Skipping ....')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()
#my_element.click()
driver.close()


#use Try and except if any ads occurs 
""" 
pip install requests
pip install bs4
pip install html5lib """