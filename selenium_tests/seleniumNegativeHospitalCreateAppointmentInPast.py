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

# navigate to hospital create doctor page
driver.get("http://localhost:8069/web#cids=1&menu_id=285&action=397&model=hospital.doctor&view_type=form")
print("Step4 passed")
time.sleep(3)
nav_bar_title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[1]/ol/li[1]/a")
nav_bar_content = nav_bar_title.text
expected_text = "Doctors"
assert expected_text in nav_bar_content, f"Expected text '{expected_text}' not found in '{nav_bar_content}'"
# The assertion will raise an AssertionError if the condition is not met.
print("Step5 passed")


# xpath changes by id of database so find input by div parent
doctor_form_input_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[1]/tbody/tr[1]/td[2]/input')
doctor_form_input_name.send_keys("Test Doctor")
time.sleep(5)
expected_doctor_text = "Test Doctor"
print("Step6 passed")
# save vehicle button
save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[1]')
save_button.click()
time.sleep(3)
print("Step7 passed")
# verify doctor name is same in show doctor details page
doctor_show_model = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[1]/tbody/tr[1]/td[2]/span')
expected_text = expected_doctor_text
assert expected_text in doctor_show_model.text, f"Expected text '{expected_text}' not found in '{doctor_show_model.text}'"
print("Step8 passed")

# verify age is 0 which is a bug. Patients are not allowed to be age 0, so validation is missing for doctors ages
doctor_age_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/table[1]/tbody/tr[2]/td[2]/span')
if doctor_age_element.text == "0":
    print("Step9 failed. Doctors age is 0. Validation missing. Negative Test")
else:
    print("Step9 passed")

# appointments page requires a doctor be created and to be in the doctor details page
schedule_appointment_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div/div/button[3]')
schedule_appointment_button.click()
time.sleep(4)
print("Step10 passed")

schedule_appointment_create_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div/div/div/main/div/div/div/div/div/div[1]/table[2]/tbody/tr[1]/td[2]/div/input')
schedule_appointment_create_date.clear()
schedule_appointment_create_date.send_keys("12/06/1066")
time.sleep(2)
print("Step11 passed")

schedule_appointment_create_save_button = driver.find_element(By.XPATH, '//*[@id="mail_activity_schedule"]')
schedule_appointment_create_save_button.click()
time.sleep(5)

past_appointment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]')
days_overdue_array = past_appointment.text.split()
for day in days_overdue_array:
    if day.isdigit():
        if int(day) > 10000:
            print("Step12 failed. Appointment is over 10000 days overdue. Validation missing. Negative Test.")
        else:
            print("Step12 passed")










driver.close()