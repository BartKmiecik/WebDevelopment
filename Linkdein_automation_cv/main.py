from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#service = Service('WebDevelopments/WebDevelopment/chromedriver.exe')
#driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location='
           'London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

while True:
    pass
