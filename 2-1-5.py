import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
    
try:

    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')

    x = x_element.text 

    # Посчитать математическую функцию от x
    y = calc(int(x)) # значение функции, которое нужно ввести в текстовое поле

    # Ввести ответ в текстовое поле
    res_input = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    res_input.send_keys(y)

    # Отметить checkbox "I'm the robot"
    checkbox_robot = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox_robot.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton_robots_rule = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton_robots_rule.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Проверяем, что смогли отправить заполненные данные формы
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    # закрываем браузер после всех манипуляций
    browser.quit()