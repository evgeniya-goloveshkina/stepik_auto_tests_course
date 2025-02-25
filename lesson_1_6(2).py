import time

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()


link = "http://suninjuly.github.io/registration2.html"

driver.get(link)
try:
    input1 = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    input3.send_keys("my_own_mail")

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    time.sleep(1)

    welcome_text_elem = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elem.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    driver.quit()

