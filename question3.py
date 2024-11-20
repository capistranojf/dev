import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login")

username = driver.find_element(By.ID,"username")
username.send_keys("student")

password = driver.find_element(By.ID,"password")
password.send_keys("Password123")

submit = driver.find_element(By.ID,"submit")
submit.click()

time.sleep(30)

driver.get("https://practicetestautomation.com/logged-in-successfully")
expected_text = "Congratulations student. You successfully logged in!"
actual_text = driver.find_element(By.ID,"error").text
assert actual_text==expected_text,"Congratulations student. You successfully logged in!"

time.sleep(30)