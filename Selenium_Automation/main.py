from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_plugin = 'C:/Users/user/Projects/Udemy_Python/WebDevelopments/WebDevelopment/Selenium_Automation/chromedriver.exe'


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")


event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
print(event_times.pop().text)

while(True):
    pass