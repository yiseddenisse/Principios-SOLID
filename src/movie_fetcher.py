from movie_scraper import extract_movie_data, download_webpage, save_movies_data

# Aplicación del principio de Single Responsibility
# Aquí solo se llama a los metodos necesarias para descargar la página web, extraer los datos de las películas y guardar los datos en un archivo CSV.
# Cada uno tiene una tarea especifica y no se encarga de más tareas de las necesarias.

def main():
    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    soup = download_webpage(url)
    movie_data = extract_movie_data(soup)
    save_movie_data(movie_data, "movie_results.csv")

if __name__ == '__main__':
    main()