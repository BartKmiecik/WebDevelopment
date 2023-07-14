from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver = webdriver.Chrome()
webdriver.get('https://orteil.dashnet.org/cookieclicker/')

btn = None
start = time.time()
should_click = False
try_clicking = True

while True:
    try:
        btn = webdriver.find_element(By.CLASS_NAME, 'fc-button-label')
        btn.click()
    except:
        try:
            cont = webdriver.find_element(By.ID, 'promptContentChangeLanguage')
            btn2 = cont.find_element(By.CSS_SELECTOR, '.langSelectButton')
            print('Button3')
            btn2.click()
        except:
            #print('smt')
            pass
    try:
        cookie = webdriver.find_element(By.ID, 'bigCookie')
        cookie.click()
    except:
        #print('No cookie :P ')
        pass
    try:
        cookies = int(webdriver.find_element(By.ID, 'cookies').text.split()[0])
        prices = webdriver.find_elements(By.CLASS_NAME, 'price')
        for n in prices:
            # print(int(n.text))
            if cookies > int(n.text):
                print(n.text)
                d = n.find_element(By.XPATH, '..')
                d.find_element(By.XPATH, '..').click()
    except:
        pass
    pass