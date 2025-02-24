import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER="37.19.220.129:8443"

options=Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")

driver=webdriver.Chrome()

driver.get("https://www.2ip.ru/")
time.sleep(5)