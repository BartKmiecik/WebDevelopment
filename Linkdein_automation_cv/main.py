# selenium 4
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
service = Service('WebDevelopments/WebDevelopment/chromedriver.exe')
# #driver = webdriver.Chrome(service=service)
# #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
driver = webdriver.Chrome(options=options, service=service)

driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location='
           'London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')
main_window = driver.current_window_handle


time.sleep(3)
log_btn = driver.find_element(By.CLASS_NAME, 'cta-modal__primary-btn')
log_btn.click()
time.sleep(3)
log_google = driver.find_element(By.CLASS_NAME, 'S9gUrf-YoZ4jf')
log_google.click()
time.sleep(3)

for handle in driver.window_handles:
    if handle != main_window:
        login_page = handle
driver.switch_to.window(login_page)
time.sleep(1)

email_input = driver.find_element(By.ID, 'identifierId')
email_input.send_keys('kmiecikjob@gmail.com')
time.sleep(1)

next_btn = driver.find_element(By.ID, 'identifierNext')
next_btn.click()
time.sleep(2)
driver.switch_to.window(main_window)

while True:
    pass
