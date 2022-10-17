#Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order.
import csv
from bs4 import BeautifulSoup
import requests

top_250_movies_url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# open the file in the write mode
with open('imdb.csv', 'w') as f:
    writer = csv.writer(f)
    header = ['title','year','rating','metascore','votes','gross','director','star actors','runtime','genre','description']
    writer.writerow(header)
    
    title = ''
    year = ''
    rating = ''
    metascore = ''
    votes = ''
    gross = ''
    director = ''
    stars = ''
    runtime = ''
    genre = ''
    description = ''

    row = [title,year,rating,metascore,votes,gross,director,stars,runtime,genre,description]
    writer.writerow(row)