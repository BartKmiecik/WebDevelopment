import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
request = requests.get(url=URL)
# print(request.text)
soup = BeautifulSoup(request.text, 'html.parser')
titles=soup.find_all(name='h3', class_='title')

list_of_100 = ''
for title in titles:
    list_of_100 += f"{title.text}\n"

print(list_of_100)

with open('movies.txt', 'w', encoding="utf-8") as file:
    file.write(list_of_100)
