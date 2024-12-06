from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_driver_path = './drivers/chromedriver/chromedriver.exe'  # Path to your ChromeDriver


# Use the Service class to specify driver path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# login to authenticate and perform operations
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
# login passed

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

# create vehicle
create_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/button")
create_button.click()
time.sleep(5)
# xpath changes by id of database so find input by div parent
vehicle_form_input_model_parent_div = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/h1/div/div[1]/div')
vehicle_form_input_model = vehicle_form_input_model_parent_div.find_element(By.TAG_NAME, "input")
vehicle_form_input_model.click()
time.sleep(1)
# dropdown is created as not sibling or child so use enter
vehicle_form_input_model.send_keys(Keys.RETURN)
time.sleep(5)
expected_model_text = "Audi/A1"
# vehicle_form_model_dropdown_item1.click()
# time.sleep(2)
print("Step6 passed")
# save vehicle button
save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]')
save_button.click()
time.sleep(3)
print("Step7 passed")
# verify model name is same in show vehicle details page
vehicle_show_model = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[4]/h1/a/span')
expected_text = expected_model_text
assert expected_text in vehicle_show_model.text, f"Expected text '{expected_text}' not found in '{vehicle_show_model.text}'"
print("Step8 passed")









driver.close()