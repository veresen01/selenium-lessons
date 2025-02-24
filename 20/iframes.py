import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--window-size=1920,1080') # устанавливаем размер окна
driver=webdriver.Chrome(options=options)

FROM_NAME_FIELD_LOCATOR=("xpath", "//input[@id='RESULT_TextField-0']")
COPY_TEXT_LOCATOR=("xpath", "//button[text()='Copy text']")
IFRAME_LOCATOR=("xpath", "//iframe")

iframe=driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(iframe)

driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one796456169")

time.sleep(3)
driver.find_element(*FROM_NAME_FIELD_LOCATOR).send_keys("Hello")
time.sleep(3)

driver.switch_to.default_content()
driver.find_element(*COPY_TEXT_LOCATOR).click()
time.sleep(3)

