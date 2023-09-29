import requests
from bs4 import BeautifulSoup as BS

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
response.encoding='utf-8'
website_html = response.text


soup = BS(website_html,'html.parser')

all_movies = soup.find_all(name='h3')


movie_titles = [movie.getText() for movie in all_movies]

movie_titles.reverse()

print(movie_titles)

with open('movies.txt',mode='a') as f:
    for movie in movie_titles:
        f.writelines(f'{movie}\n')


