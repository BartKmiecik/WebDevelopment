import requests
from bs4 import BeautifulSoup

date = input('What day you want to go back in time? YYYY-MM-DD')
#2000-09-02/
url = f'https://www.billboard.com/charts/hot-100/{date}'
request = requests.get(url=url)

soup = BeautifulSoup(request.text, 'html.parser')
titles = soup.select('ul li ul li h3', class_='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')
#titles = soup.find_all(name='h3', id='title-of-a-story', class_='c-title  a-no-trucate')
for title in titles:
    print(title.text.strip())
