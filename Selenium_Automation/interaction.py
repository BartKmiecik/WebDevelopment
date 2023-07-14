from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()

webdriver.get('https://en.wikipedia.org/wiki/Main_Page')

header_section = webdriver.find_element(By.CSS_SELECTOR, '.mp-box')
whole_line = header_section.find_element(By.ID, 'articlecount')
number = whole_line.find_element(By.CSS_SELECTOR, 'a')
print(int(number.text.replace(',', '')))

while True:
    pass