# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
service = Service('WebDevelopments/WebDevelopment/chromedriver.exe')
# #driver = webdriver.Chrome(service=service)
# #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=service)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location='
           'London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')


while True:
    pass
