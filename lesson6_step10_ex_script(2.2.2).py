#!/usr/bin/python3
import time
import math

from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)


    check1 = browser.find_element_by_css_selector("[id = 'robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check1)
    check1.click()

    radio1= browser.find_element_by_css_selector("[for = 'robotsRule']")
    radio1.click()


    button = browser.find_element_by_css_selector("button.btn")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.quit()


