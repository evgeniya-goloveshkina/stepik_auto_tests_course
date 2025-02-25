from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")

# Задача — кликнуть на перекрытую кнопку
# В метод execute_script мы передаём текст js-скрипта и найденный элемент button,
# к которому нужно будет проскроллить страницу.
# После выполнения кода элемент button должен оказаться в верхней части страницы.
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. Эта команда проскроллит страницу на 100 пикселей вниз:
#browser.execute_script("window.scrollBy(0, 100);")

button.click()