import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--window-size=1920,1080') # устанавливаем размер окна
driver_1=webdriver.Chrome(options=options)

LOGIN_FIELD=("xpath", "//input[@type='email']")
PASSWORD_FIELD=("xpath", "//input[@type='password']")
SUBMIT_BUTTON=("xpath", "//button[@type='submit']")

driver_1.get("https://hyperskill.org/login")
driver_1.find_element(*LOGIN_FIELD).send_keys("V4m5t@example.com")
driver_1.find_element(*PASSWORD_FIELD).send_keys("password")
driver_1.find_element(*SUBMIT_BUTTON).click()
time.sleep(3)


driver_2=webdriver.Chrome(options=options)
driver_2.get("https://hyperskill.org/login")
time.sleep(3)