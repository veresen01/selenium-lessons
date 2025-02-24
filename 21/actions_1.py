import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action=ActionChains(driver)

LEFT_BUTTON_LOCATOR=("xpath", "//button[@id='leftClick']")
DOUBLE_LEFT_BUTTON_LOCATOR=("xpath", "//button[@id='doubleClick']")
RIGHT_BUTTON_LOCATOR=("xpath", "//button[@id='rightClick']")
HOVER_BUTTON_LOCATOR=("xpath", "//button[@id='colorChangeOnHover']")                           

driver.get("https://testkru.com/Elements/Buttons")

left_button=driver.find_element(*LEFT_BUTTON_LOCATOR)
double_button=driver.find_element(*DOUBLE_LEFT_BUTTON_LOCATOR)
right_button=driver.find_element(*RIGHT_BUTTON_LOCATOR)
hover_button=driver.find_element(*HOVER_BUTTON_LOCATOR)

action.click(left_button).perform() # кликаем левой кнопкой
time.sleep(3)


action.double_click(double_button).perform() # кликаем левой кнопкой дважды
time.sleep(3)


action.context_click(right_button).perform() # кликаем правой кнопкой
time.sleep(3)

action.move_to_element(hover_button).perform() # наводим на кнопку
time.sleep(3)

# action.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button).perform() # кликаем поочереди все

