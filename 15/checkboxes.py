import time
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from    selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
wait= WebDriverWait(driver,10, poll_frequency=1)


# CHECKBOX_1=("xpath","//input[@type='checkbox'][1]")

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# 1 способ
# time.sleep(3)
# print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# time.sleep(3)

# 2 способ
# print(driver.find_element(*CHECKBOX_1).is_selected())
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).is_selected())
# time.sleep(3)


# 3способ
# CHECKBOX_home_STATUS=("xpath","//input[@id='tree-node-home']")
# CHECKBOX_home_ACTION=("xpath","//span[@class='rct-checkbox']")
# driver.get("https://demoqa.com/checkbox")
# print(driver.find_element(*CHECKBOX_home_STATUS).is_selected())
# driver.find_element(*CHECKBOX_home_ACTION).click()
# print(driver.find_element(*CHECKBOX_home_STATUS).is_selected())
# time.sleep(3)

# радиокнопка
YES_RADIO_STATUS=("xpath","//input[@id='yesRadio']")
YES_RADIO_ACTION=("xpath","//label[@for='yesRadio']")

NO_RADIO_STATUS=("xpath","//input[@id='noRadio']")
NO_RADIO_ACTION=("xpath","//label[@for='noRadio']")
driver.get("https://demoqa.com/radio-button")

print(driver.find_element(*YES_RADIO_STATUS).is_selected())
driver.find_element(*YES_RADIO_ACTION).click()
print(driver.find_element(*YES_RADIO_STATUS).is_selected())
time.sleep(3)
