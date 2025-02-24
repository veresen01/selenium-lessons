from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select 
import time
from selenium.webdriver.common.keys import Keys


service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)


# KEYBOARD_INPUT=("xpath","//input[@id='target']")
# driver.get("https://the-internet.herokuapp.com/key_presses")
# time.sleep(3)
# driver.find_element(*KEYBOARD_INPUT).send_keys("Hello")
# time.sleep(3)

# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.Control + "a")
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACK_SPACE)
# time.sleep(3)


# SELECT_LOCATOR=("xpath","//select[@id='react-select-3-input']")
# driver.get("https://demoqa.com/select-menu")
# time.sleep(3)
# driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
# driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
# time.sleep(3)

# мультивыбор
MULTISELECT_LOCATOR=("xpath","//input[@id='react-select-4-input']")
driver.get("https://demoqa.com/select-menu")

driver.find_element(*MULTISELECT_LOCATOR).send_keys("Green")
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
time.sleep(3)

