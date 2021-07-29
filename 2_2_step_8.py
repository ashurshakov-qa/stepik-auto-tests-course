import time
import os

from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element_by_css_selector('input[name="firstname"]').send_keys('First name')
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Last name')
    browser.find_element_by_css_selector('input[name="email"]').send_keys('Email')

    browser.find_element_by_id('file').send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt'))

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()

#