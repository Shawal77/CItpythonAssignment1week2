#Scrap Hacker News project and save the result in a csv file. The csv file should have the following columns: title, link, points, comments, author, rank. The csv file should be sorted by rank in ascending order.
import csv
from bs4 import BeautifulSoup
import requests

title = ''
link = ''
points = ''
comments = ''
author = ''
rank = ''

hacker_news_url = 'https://news.ycombinator.com/'
header = [title, link, points, comments, author, rank]
