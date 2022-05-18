from selenium import webdriver
import time
import math


def calc(attr):
    return math.log(abs(12 * math.sin(attr)))


try:
    link = 'https://suninjuly.github.io/execute_script.html'

    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем значение х и пропускаем его через функцию calc
    x = int(browser.find_element_by_id('input_value').text)
    input_text = browser.find_element_by_id('answer')
    # Подставляем значение в поле ввода
    input_text.send_keys(str(calc(x)))

    # Ставим галочку на checkbox
    browser.find_element_by_id('robotCheckbox').click()

    # Скроллим до скрытого элемента
    browser.execute_script('window.scrollBy(0, 100);')

    # Ставим галочку на radiobutton
    browser.find_element_by_id('robotsRule').click()

    # Отправляем заполненную форму
    browser.find_element_by_css_selector('button.btn').click()

finally:

    time.sleep(5)
    browser.quit()
