from bs4 import BeautifulSoup
import requests
# with open(file='website.html') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# print(soup.title)

#

request = requests.get('https://news.ycombinator.com/')
web = request.text

soup = BeautifulSoup(web, 'html.parser')
# print(soup)
article_tag = soup.find_all(name='a', rel='noreferrer')
article_texts = []
article_links = []
for article in article_tag:
    article_texts.append(article.get_text())
    article_links.append(article.get('href'))
# print(article_link)
scores = soup.select('.score')
num_scores = []
for score in scores:
    temp_score = int(score.text.split(' ')[0])
    print(temp_score)
    num_scores.append(temp_score)

max_score = max(num_scores)
max_index = num_scores.index(max_score)
print(f'Max score is {max_score} with index of {max_index}')
print(scores[max_index])

print(f'\n\n\n{article_texts[max_index]} \n{article_links[max_index]}\n{num_scores[max_index]}')