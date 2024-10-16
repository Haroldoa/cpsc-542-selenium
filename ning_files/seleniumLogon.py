from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('./drivers/chromedriver')
driver.get("http://localhost:8069/web/login")
print(driver.title)
#search_bar = driver.find_element_by_name("q")

driver.get("http://localhost:8069/web/login")
print("Ning: Step1 passed")


search_bar = driver.find_element(By.NAME, "login")
search_bar.clear()
time.sleep(3)
search_bar.send_keys("somesite.com")
print("Ning: Step2 passed")
time.sleep(3)

search_bar = driver.find_element(By.NAME, "password")
print("Ning: Step3 passed")
time.sleep(3)
search_bar.send_keys("yourpassword")
time.sleep(3)
#search_bar.clear()
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.current_url)
driver.close()