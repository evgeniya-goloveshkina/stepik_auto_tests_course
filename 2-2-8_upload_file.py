import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_firstname = browser.find_element(By.CSS_SELECTOR, "[name=\"firstname\"]")
    input_firstname.send_keys("Имя")

    input_lastname = browser.find_element(By.CSS_SELECTOR, "[name=\"lastname\"]")
    input_lastname.send_keys("Фам")

    input_email = browser.find_element(By.CSS_SELECTOR, "[name = \"email\"]")
    input_email.send_keys("1@m.ru")

    with open("test.txt", "w") as file:
        content = file.write("automation by python") 

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)

    input5 = browser.find_element(By.CSS_SELECTOR, '[id="file"]')
    input5.send_keys(file_path)

    # Нажать кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    time.sleep(1)

    # Скопировать из алерта число для ответа
    print(browser.switch_to.alert.text.split()[-1])

    os.remove("test.txt")  # удаляем

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

    browser.quit()