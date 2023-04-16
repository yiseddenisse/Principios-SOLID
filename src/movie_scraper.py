import requests
import re
import csv
from bs4 import BeautifulSoup
from datos_pelicula import Data

# Aplicación del principio de Single Responsibility
# Aquí solo se llama a los metodos necesarias.Cada uno tiene una tarea especifica y no se encarga de más tareas de las necesarias.

#Descarga una pagina web y regresa su contenido como un objeto BeautifuSoup
def download_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

#Extrae los detalles de una pelicula y regresa un diccionario
def get_movie_details(movie):
    movie_string = movie.get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]

    data = {"movie_title": movie_title,
            "year": year,
            "place": place}
    return data

def extract_movie_data(soup):
    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    movie_data = []
    for index in range(0, len(movies)):
        movie = movies[index]
        details = get_movie_details(movie)
        details["star_cast"] = crew[index]
        details["rating"] = ratings[index]
        details["vote"] = votes[index]
        details["link"] = links[index]
        details["preference_key"] = index % 4 + 1
        movie_data.append(details)

    return movie_data


def scrape_movies(url):
    movies, links, crew, ratings, votes = extract_movie_data(soup)
    return [Data(**get_movie_details(movies[i], i, crew, ratings, votes, links)) for i in range(len(movies))]

#Metodo que guarda los datos en un archivo CSV
def save_movie_data(movie_data, filename):
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in movie_data:
            writer.writerow(movie)