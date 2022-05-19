import pytest
from selenium import webdriver
import time
import math

links_list = ['https://stepik.org/lesson/236895/step/1',
              'https://stepik.org/lesson/236896/step/1',
              'https://stepik.org/lesson/236897/step/1',
              'https://stepik.org/lesson/236898/step/1',
              'https://stepik.org/lesson/236899/step/1',
              'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1',
              'https://stepik.org/lesson/236905/step/1']


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', links_list)
class TestHomeWork:
    def test_guest_should_see_login_link(self, browser, links):
        answer = math.log(int(time.time()))
        browser.get(links)
        browser.find_element_by_tag_name("textarea").send_keys(str(answer))
        browser.find_element_by_css_selector('.submit-submission').click()
        error_res = browser.find_element_by_css_selector('.smart-hints__hint').text

        assert error_res == "Correct!", f'Ошибочка вышла, кто-то захватил тесты.. Наверное инопланетяне! {error_res}'
