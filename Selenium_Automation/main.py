from selenium import webdriver

chrome_plugin = 'Selenium_Automation/chromedriver.exe'

driver = webdriver.Chrome(chrome_plugin)

driver.get('http://www.google.com/')

