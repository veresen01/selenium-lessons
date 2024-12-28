from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from    selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless') # отключаем отображение браузера. в фоне
options.add_argument('--window-size=1920,1080') # устанавливаем размер окна
options.add_argument('--disable-blink-features=AutomationControlled') # отключаем автоматизацию.сайт думает что человек работает
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.3') # устанавливаем User-Agent

service=Service(executable_path=ChromeDriverManager().install()) # устанавливаем драйвер
driver=webdriver.Chrome(service=service,options=options)
wait=WebDriverWait(driver, 5,poll_frequency=1) # устанавливаем ожидание

driver.get('https://whatismyipaddress.com') # открываем сайт
time.sleep(3)   


# driver.get('https://ya.ru')

# driver.save_screenshot('ya.png') # делаем скриншот




