import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--window-size=1920,1080') # устанавливаем размер окна
driver=webdriver.Chrome(options=options)

# FOR_BUISNES_BUTTON_LOCATOR=("xpath", "(//a[text()='Для бизнеса'])")
# START_FREE_BUTTON_LOCATOR=("xpath", "(//a[text()='Начать бесплатно'])")

# driver.get("https://hyperskill.rorg/tracks/")
# time.sleep(3)
# # print(driver.current_window_handle) #получаем id активного окна
# print(driver.window_handles) #получаем id всех окон


# driver.find_element(*FOR_BUISNES_BUTTON_LOCATOR).click()
# time.sleep(3)

# tabs=driver.window_handles

# driver.switch_to.window(tabs[1])

# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
# time.sleep(3)

# # если 2 окна
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# driver.get("https://www.ya.ru/")
# time.sleep(3)


driver.switch_to.new_window('tab')