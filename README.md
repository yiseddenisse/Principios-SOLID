# RESPUESTA A LAS PREGUNTAS DEL PUNTO 1 DE LA TAREA
Analiza el funcionamiento del script.
¿Cual es su entrada? El script descarga los datos de la página web 'http://www.imdb.com/chart/top', que contiene información de las 250 mejores películas según la base de datos de Internet Movie Database (IMDb).
¿Que procesamiento esta haciendo? El script utiliza la biblioteca BeautifulSoup para extraer información de la página web. 
La información extraída incluye el título, el año de estreno, el lugar en el ranking, el reparto, la valoración y el número de votos recibidos. Esta información se almacena en una lista de diccionarios.
¿Cual es su salida? El script guarda los datos de la lista de diccionarios en un archivo CSV llamado "movie_results.csv".


# RAZONES POR LAS QUE CUMPLE CON LOS PRINCIPIOS SOLID
1. Single Responsibility: El script original se dividió en diferentes funciones o clases que se encargan de tareas específicas, como descargar la página web, extraer la información de la página, guardar la información en un archivo CSV, entre otras, descritas en el codigo.

2. Open Closed: El código esta escrito para poder extenderlo y añadir nuevas funcionalidades. Por ejemplo, se podrían añadir funciones para filtrar las películas por género o director, o para descargar información adicional, pero esta cerrado para hacerle modificaciones

3. Liskov Substitution: Las funciones del programa que lo componen pueden ser reutilizadas en diferentes contextos sin afectar su funcionamiento. Por ejemplo, se podrían reutilizar las funciones de extracción de información de la página web en otro script que descargue información de otra fuente.

4. Interface Segregation: Las interfaces del codigo son específicas para cada tarea, y se puede observar que no se incluyen metodos innecesarios. 

5. Dependency Inversion: Los módulos de bajo nivel no dependan de los módulos de alto nivel. 

# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME