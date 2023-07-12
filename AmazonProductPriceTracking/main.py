import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'Accept-Language':'pl-PL,pl;q=0.5',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
request = requests.get('https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6', headers=headers)
soup = BeautifulSoup(request.text, 'lxml')


whole_price = (soup.find(name='span', class_='a-price-whole').text)
fraction_price = (soup.find(name='span', class_='a-price-fraction').text)
price = float(f'{whole_price}{fraction_price}')

print(price)


