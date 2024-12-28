from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/pl") 

driver.find_element("id","loginformsubmit").click() # поиск элемента и нажатие на него, кнопка логин "loginformsubmit"
time.sleep(3)   