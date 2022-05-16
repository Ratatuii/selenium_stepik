from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для переменной x.
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute('valuex')

    # Ищем поле для ввода.
    input_text = browser.find_element_by_id("answer")

    # Считаем значение функции от x.
    input_text.send_keys(calc(x))

    # Ставим галочку на I'm the robot
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    # Ставим галочку на Robots rule
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
