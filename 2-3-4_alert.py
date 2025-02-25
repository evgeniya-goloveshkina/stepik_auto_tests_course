from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math
def calc_in_string(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    submit_button_initial = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button_initial.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text # атрибут .text для найденного элемента

    answer = calc_in_string(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_answer.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    print(browser.switch_to.alert.text)

    # Проверяем, что смогли отправить заполненные данные формы
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()