import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

try:
    browser.get(link)

    button_verify = browser.find_element(By.CSS_SELECTOR, "#verify")
    button_verify.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()
