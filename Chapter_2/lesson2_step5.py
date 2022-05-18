from selenium import webdriver
import time
import math
import os

def calc(attr):
    return math.log(abs(12 * math.sin(attr)))


try:
    link = 'https://suninjuly.github.io/file_input.html'

    browser = webdriver.Chrome()
    browser.get(link)
    print(os.path.abspath(__file__))

    # Ищем значение х и пропускаем его через функцию calc
    x = browser.find_elements_by_css_selector("input[type='text']")
    for i in x:
        i.send_keys('Aaaaaaa')

    file = browser.find_element_by_css_selector("input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '../test.txt')
    file.send_keys(file_path)
    # Отправляем заполненную форму
    browser.find_element_by_css_selector('button.btn').click()

finally:

    time.sleep(5)
    browser.quit()
