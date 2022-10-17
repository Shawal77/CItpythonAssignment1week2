#Scrap Hacker News project and save the result in a csv file. The csv file should have the following columns: title, link, points, comments, author, rank. The csv file should be sorted by rank in ascending order.
import csv
from bs4 import BeautifulSoup
import requests
import re

hacker_news_url = 'https://news.ycombinator.com/'
header = ['Title', 'Link', 'Points', 'Comments', 'Author', 'Rank']

html_data = requests.get(hacker_news_url).text
soup = BeautifulSoup(html_data,'lxml')

news_articles = soup.find_all('tr',class_="athing")
sublines = soup.find_all('td',class_="subtext")


with open('hacker_news.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for news_article in news_articles:
        title = news_article.find('span',class_='titleline').a.text
        link = news_article.find('span',class_='titleline').a['href']
        rank = news_article.find('span',class_='rank').text

        for subline in sublines:
            points = subline.find('span',class_='score').text
            anchor = subline.find_all('a')
            comments_text = anchor[-1].text
            comments = re.search("\d+", comments_text).group()
            author = subline.find('a',class_='hnuser').text
            break
        
        row = [title, link, points, comments, author, rank]
        writer.writerow(row)