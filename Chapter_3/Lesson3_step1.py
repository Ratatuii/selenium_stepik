import unittest
from selenium import webdriver
import pytest


def py_tests(link):
    browser = webdriver.Chrome()
    browser.get(link)
    # Код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".first_block .form-control.first:required")
    first_name.send_keys('first name')
    last_name = browser.find_element_by_css_selector(".first_block .form-control.second:required")
    last_name.send_keys('Last name')
    email = browser.find_element_by_css_selector(".first_block .form-control.third:required")
    email.send_keys('email@email.co')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    welcome_text = browser.find_element_by_tag_name("h1").text
    browser.quit()
    return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "https://suninjuly.github.io/registration1.html"
        tests_result = py_tests(link)

        self.assertEqual("Congratulations! You have successfully registered!", tests_result, "Ошибочка вышла на тесте")

    def test_abs2(self):
        link = "https://suninjuly.github.io/registration2.html"
        tests_result = py_tests(link)

        self.assertEqual("Congratulations! You have successfully registered!", tests_result, "Ошибочка вышла")


if __name__ == "__main__":
    unittest.main()
