import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
email = 'mlodybartus@gmail.com'
password = 'tkelpunbstudhbgo'
amazon_headers = {
    'Accept-Language':'pl-PL,pl;q=0.5',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
request = requests.get(url, headers=amazon_headers)
soup = BeautifulSoup(request.text, 'lxml')
treshold = 100

whole_price = (soup.find(name='span', class_='a-price-whole').text.strip())
fraction_price = (soup.find(name='span', class_='a-price-fraction').text.strip())
price = float(f'{whole_price}{fraction_price}')
product_title = soup.find(name='span', id='productTitle').text.strip()

if price < treshold:
    msg = f'Product on sale\n\n {product_title} is for {price} at {url}'.encode('utf-8')
    print(msg)
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(user=email, password=password)
        smtp.sendmail(email,email,msg)
        print(msg)


        





