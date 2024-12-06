from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_driver_path = '../ning_files/drivers/chromedriver/chromedriver.exe'  # Path to your ChromeDriver


# Use the Service class to specify driver path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://localhost:8069/web/login")
print(driver.title)
#search_bar = driver.find_element_by_name("q")

driver.get("http://localhost:8069/web/login")
print("Step1 passed")


search_bar = driver.find_element(By.NAME, "login")
search_bar.clear()
time.sleep(3)
search_bar.send_keys("haroldoalt@gmail.com")
print("Step2 passed")
time.sleep(3)

search_bar = driver.find_element(By.NAME, "password")
print("Step3 passed")
time.sleep(3)
search_bar.send_keys("openpgpwd")
time.sleep(3)
#search_bar.clear()
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.current_url)


# navigate to fleet
driver.get("http://localhost:8069/web#menu_id=97&action=128")
print("Step4 passed")
time.sleep(3)
nav_bar_title = driver.find_element(By.XPATH, "/html/body/header/nav/a")
nav_bar_content = nav_bar_title.text
expected_text = "Fleet"
assert expected_text in nav_bar_content, f"Expected text '{expected_text}' not found in '{nav_bar_content}'"
# The assertion will raise an AssertionError if the condition is not met.
print("Step5 passed")
driver.close()