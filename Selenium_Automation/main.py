from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_plugin = 'C:/Users/user/Projects/Udemy_Python/WebDevelopments/WebDevelopment/Selenium_Automation/chromedriver.exe'


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")


event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
for n in range(len(event_times)):
    print(event_times[n].text, event_names[n].text)

while(True):
    pass