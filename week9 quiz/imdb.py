#Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order.
import csv
from bs4 import BeautifulSoup
import requests

top_250_movies_url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'
html_data = requests.get(top_250_movies_url).text
soup = BeautifulSoup(html_data,'lxml')
movies = soup.find_all('tr')
# open the file in the write mode
with open('imdb.csv', 'w') as f:
    writer = csv.writer(f)
    header = ['title','year','rating','metascore','votes','gross','director','star actors','runtime','genre','description']
    writer.writerow(header)
    for movie in movies:
        title = movie.find('td',class_='titleColumn').a.text
        link= movie.find('td',class_='titleColumn').a['href']
        year = movie.find('span',class_='secondaryInfo')
        rating = movie.find('td',class_="ratingColumn imdbRating").strong
        
        details = requests.get(link)
        detailed_soup = BeautifulSoup(details,'lxml')
        metascore = detailed_soup.find('span',class_="score-meta").text
        
        votes = detailed_soup.find('span',class_="score")
        
        gross = detailed_soup.find('span',class_ = "ipc-metadata-list-item__list-content-item").text
        
        director = detailed_soup.find('a',class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
        
        stars = detailed_soup.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt").text
        
        runtime = detailed_soup.find('div',class_ = "ipc-metadata-list-item__content-container").text
        
        genre = detailed_soup.find('a',class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
        
        description = detailed_soup.find('span',class_="sc-16ede01-1 kgphFu")

        row = [title,year,rating,metascore,votes,gross,director,stars,runtime,genre,description]
        writer.writerow(row)