from selenium import webdriver
import time
import math

def calc(attr):
    return math.log(abs(12 * math.sin(attr)))


try:
    link = 'https://suninjuly.github.io/alert_accept.html'

    browser = webdriver.Chrome()
    browser.get(link)
    # Ищем кнопку и кликаем на неё
    browser.find_element_by_css_selector('button.btn').click()
    # Переключаемся на окно подтверждения и подтверждаем его
    confirm = browser.switch_to.alert
    confirm.accept()
    # Идем значение х и переводим его в формат int
    x = int(browser.find_element_by_id('input_value').text)

    # Ищем поле ввода для х и пропуская его через функцию calc вводим
    browser.find_element_by_css_selector("input[type='text']").send_keys(str(calc(x)))

    # Отправляем заполненную форму
    browser.find_element_by_css_selector('button.btn').click()

finally:

    time.sleep(5)
    browser.quit()
