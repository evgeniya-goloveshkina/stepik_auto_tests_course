import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    element = browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = element.get_attribute("valuex")

    # Посчитать математическую функцию от x
    y = calc(x) # значение функции, которое нужно ввести в текстовое поле

    # Ввести ответ в текстовое поле
    res_input = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    res_input.send_keys(y)

    # Отметить checkbox "I'm the robot"
    checkbox_robot = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    checkbox_robot.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton_robots_rule = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
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

# не забываем оставить пустую строку в конце файл