from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math
def calc_in_string(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text  # атрибут .text для найденного элемента

    answer = calc_in_string(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_answer.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
