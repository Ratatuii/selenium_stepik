from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значения для переменных, а и b.
    a_element = int(browser.find_element_by_id("num1").text)
    b_element = int(browser.find_element_by_id("num2").text)

    # Выбираем список и выполняем поиск в нем по значению, можно было по тексту
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(a_element + b_element))

    # Отправляем
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Радуемся :)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
