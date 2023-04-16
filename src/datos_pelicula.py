class Data:
#Aplicacion del principio SOLID
# Aplicacion del principio Open Closed pues esta clase no es necesario de modificar pero si se puede usar en cualquier otro lugar
    def __init__(self, movie_title, year, place, star_cast, rating, vote, link, preference_key):
        self.movie_title = movie_title
        self.year = year
        self.place = place
        self.star_cast = star_cast
        self.rating = rating
        self.vote = vote
        self.link = link
        self.preference_key = preference_key

    def list_atributos(self):
        return {"movie_title": self.movie_title,
                "year": self.year,
                "place": self.place,
                "star_cast": self.star_cast,
                "rating": self.rating,
                "vote": self.vote,
                "link": self.link,
                "preference_key": self.preference_key}