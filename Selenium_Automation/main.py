from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_plugin = 'C:/Users/user/Projects/Udemy_Python/WebDevelopments/WebDevelopment/Selenium_Automation/chromedriver.exe'


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")


while(True):
    pass