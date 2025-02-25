from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

class CustomBrowser(webdriver.Chrome):
    def solve_captcha(self):
        value_x = int(self.find_element(By.ID, "input_value").text)
        #value_x = int(self.find_element_by_id("input_value").text)
        value_x = math.log(abs(12*math.sin(value_x)))
        field_input = self.find_element(By.ID, "answer").send_keys(str(value_x))

browser = CustomBrowser()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    #  функция until, в которую передается правило ожидания,
    #  элемент, а также значение, по которому мы будем искать элемент

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    browser.solve_captcha()

    submit_answer_button = browser.find_element(By.ID, "solve")
    submit_answer_button.click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()