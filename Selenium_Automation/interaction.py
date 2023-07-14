from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()

webdriver.get('http://secure-retreat-92358.herokuapp.com/')
#
# header_section = webdriver.find_element(By.CSS_SELECTOR, '.mp-box')
# whole_line = header_section.find_element(By.ID, 'articlecount')
# number = whole_line.find_element(By.CSS_SELECTOR, 'a')
# number.click()
# print(int(number.text.replace(',', '')))
name = webdriver.find_element(By.NAME, 'fName')
name.send_keys('Bart')
sur = webdriver.find_element(By.NAME, 'lName')
sur.send_keys('Kmie')
email = webdriver.find_element(By.NAME, 'email')
email.send_keys('email@gmail.com')
btn = webdriver.find_element(By.CLASS_NAME, 'btn')
btn.click()


while True:
    pass