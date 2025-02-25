from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
browser.execute_script("document.title='Script executing';alert('Robots at work');")
browser.quit()

alert = browser.switch_to.alert
alert.accept()