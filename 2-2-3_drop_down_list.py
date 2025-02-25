import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc_sum(x, y):
  return x + y

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной num1, num2
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    y_element = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')

    num1 = x_element.text # атрибут .text для найденного элемента
    num2 = y_element.text # атрибут .text для найденного элемента

    # Посчитать математическую функцию от x
    y = str(calc_sum(int(num1), int(num2))) # значение функции, которое нужно ввести в текстовое поле

    # Инициализировать новый объект, передав в него WebElement с тегом select
    select = Select(browser.find_element(By.TAG_NAME, "select"))

    # Выбрать ответ
    select.select_by_value(str(y))  # ищем элемент с текстом "y"
  
    #browser.find_element(By.CSS_SELECTOR, "[value='" + y + "']").click()
    #select.select_by_visible_text(str(y))

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