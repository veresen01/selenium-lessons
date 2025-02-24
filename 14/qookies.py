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

driver.get("https://www.freeconferencecall.com/en/us/login")
# print(driver.get_cookie("country_code"))

# driver.add_cookie({
#     "name":"EXample",
#     "value":"KuKu"
# })

# print(driver.get_cookie("EXample"))





# before=driver.get_cookie("split")
# print(before)

# driver.delete_cookie("split")
# driver.add_cookie({
#     "name":"split",
#     "value":"qwerty"
# })

# after=driver.get_cookie("split")
# print(after)



