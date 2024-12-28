from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

chrome_options = webdriver.ChromeOptions()

# prefs={"download.default_directory": f'{os.getcwd()}/downloads'}
prefs = {'download.default_directory' : '/path/to/dir'}

chrome_options.add_experimental_option("prefs",prefs)



service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)

driver.find_elements(By.XPATH,'//a')[3].click()

time.sleep(3)


