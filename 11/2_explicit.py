from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from    selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
wait=WebDriverWait(driver, 15,poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")


REMOVE_BUTTON=(By.XPATH, '//button[@id="remove"]')

driver.find_element(*REMOVE_BUTTON).click()
wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))


