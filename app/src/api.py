"""
Module des appels aux différentes apis
"""

import requests

from conf import url_themoviedb_api, themovedb_api_key

# Le cache pour les films (clé: imdb id)
movies_cache = {}

# Le cache pour les personnes (clé: id de la personne)
people_cache = {}

def is_person_in_cache(id):
    """
    Retourne vrai si la personne avec l'identifiant en paramètre est déjà dans le cache, faux sinon
    """
    for cached_person_id in people_cache:
        if cached_person_id == id:
            return True
    return False


def get_person(id):
    """
    Retourne les informations d'une personne, charge la personne dans le cache si elle n'est pas présente
    """
    if not is_person_in_cache(id):
        people_cache[id] = requests.get(url_themoviedb_api + "person/" + str(id) + "?api_key=" + themovedb_api_key).json()
    return people_cache[id]


def get_movie_crew(movie):
    movie_id = requests.get(url_themoviedb_api + "find/" + movie['imdbID'] + "?external_source=imdb_id&api_key=" + themovedb_api_key).json()['movie_results'][0]['id']

    movie_credits = requests.get(url_themoviedb_api + "movie/" + str(movie_id) + "/credits?api_key=" + themovedb_api_key).json()['cast']
    
    movie_crew = []

    for person in movie_credits:
        movie_crew.append(get_person(person['id']))

    return movie_crew
