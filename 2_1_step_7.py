import time
import math

from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    result = calc(browser.find_element_by_id('treasure').get_attribute('valuex'))
    browser.find_element_by_id('answer').send_keys(str(result))

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()

#