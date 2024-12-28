from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()  # создаем объект опций
chrome_options.page_load_strategy="normal"  # устанавливаем стратегию загрузки страницы
# chrome_options.add_argument("--headless")  # отключаем отображение браузера. в фоне
# chrome_options.add_argument("--incognito")  # запускаем в инкогнито
# chrome_options.add_argument("--ignored-certificate-errors") # игнорируем ошибки 
# chrome_options.add_argument("--window-size=1920,1080") #  устанавливаем размер окна
# chrome_options.add_argument("--disable-cashes") # отключаем кэши
service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()

driver.get("https://www.hyperskill.org/tracks")

end_time = time.time()
print(end_time - start_time)


