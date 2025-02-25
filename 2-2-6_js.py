import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')

    x = x_element.text # атрибут .text для найденного элемента

    # Посчитать математическую функцию от x
    y = calc(int(x)) # значение функции, которое нужно ввести в текстовое поле

    # Ввести ответ в текстовое поле
    res_input = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    res_input.send_keys(y)

    # Проскроллить страницу вниз, чтобы кликнуть на перекрытый элемент
    # В метод execute_script мы передаём текст js-скрипта и найденный элемент button,
    # к которому нужно будет проскроллить страницу.
    # После выполнения кода элемент должен оказаться в верхней части страницы.

    # Отметить checkbox "I'm the robot"
    checkbox_robot = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_robot)
    checkbox_robot.click()

    # Переключить radiobutton "Robots rule!"
    radiobutton_robots_rule = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton_robots_rule.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Проверяем, что смогли отправить заполненные данные формы
    # ждем загрузки страницы
    time.sleep(1)

    # Если вы не успеваете отрабатывать задание по времени, чтобы скопировать из алерта число для ответа,
    # то это можно сделать с помощью следующей команды, которую необходимо использовать после вашего кода,
    # имитирующего нажатие на кнопку "Submit".
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()