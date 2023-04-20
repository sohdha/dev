from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/soham/OneDrive/Desktop/login.html")
time.sleep(4)
driver.find_element("name", "username").send_keys("soham")
time.sleep(4)
driver.find_element("name", "password").send_keys("dhaware")
time.sleep(4)

driver.find_element("name", "btnK").send_keys(Keys.ENTER)
time.sleep(4)

driver.close()
print("sample test case successfully completed")