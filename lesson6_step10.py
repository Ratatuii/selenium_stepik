from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Ищем поле для ввода.
    input_text = browser.find_element_by_id("answer")

    # Считаем значение функции от x.
    input_text.send_keys(calc(x))

    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
