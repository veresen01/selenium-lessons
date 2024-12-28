from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://catapulto.ru/") 
login_button=driver.find_element(By.XPATH,'//a[@id="menu_login_button"]') #ищем элемент с идентификатором "menu_login_button" по xpath
login_button.click()
email_field=driver.find_element(By.XPATH,'//div[@id="root"]/div/div[4]/div[1]/div/div/div/div/form/div/div[1]/div') # ищем поле email с по xpath
email_field.send_keys("admin@admin.ru") #вводим email
print(email_field.get_attribute("value")) #выводим email
time.sleep(3)

email_field.clear() #очищаем поле email
email_field.send_keys("admin") #вводим email