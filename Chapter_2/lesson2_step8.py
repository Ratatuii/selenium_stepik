from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math


def calc(attr):
    return math.log(abs(12 * math.sin(attr)))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)
try:
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    # Ищем кнопку и кликаем на неё
    browser.find_element_by_id('book').click()

    # Ищем значение х и пропускаем его через функцию calc
    x = calc(int(browser.find_element_by_id('input_value').text))
    input_text = browser.find_element_by_id('answer')
    # Подставляем значение в поле ввода
    input_text.send_keys(str(x))
    browser.execute_script('window.scrollBy(0, 100);')

    # Отправляем заполненную форму
    browser.find_element_by_id('solve').click()
    time.sleep(4)

finally:
    browser.quit()
