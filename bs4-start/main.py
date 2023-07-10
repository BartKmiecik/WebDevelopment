from bs4 import BeautifulSoup

with open(file='website.html') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print(soup.title)