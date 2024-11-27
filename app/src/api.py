"""
Module des appels aux différentes apis
"""

import requests
from copy import deepcopy

from conf import url_themoviedb_api, themoviedb_api_key

# Le cache pour les films (clé: imdb id)
movies_cache = {}

# Le cache pour les personnes (clé: id de la personne)
people_cache = {}

# Les métiers qui nous intéresse uniquement
crew_jobs = ["director", "producer", "editor"]

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
        people_cache[id] = requests.get(url_themoviedb_api + "/person/" + str(id) + "?api_key=" + themoviedb_api_key).json()
    return people_cache[id]


def get_movie_crew(movie):
    try:
        movie_id = requests.get(url_themoviedb_api + "/find/" + movie['imdbID'] + "?external_source=imdb_id&api_key=" + themoviedb_api_key).json()['movie_results'][0]['id']

        credits = requests.get(url_themoviedb_api + "/movie/" + str(movie_id) + "/credits?api_key=" + themoviedb_api_key).json()
        
        movie_crew = []

        for actor in credits['cast']:
            person = deepcopy(get_person(actor['id']))
            person['job'] = "actor"
            movie_crew.append(person)

        for crew_member in credits['crew']:
            job = crew_member['job'].lower()
            if job in crew_jobs:
                person = deepcopy(get_person(crew_member['id']))
                person['job'] = job
                movie_crew.append(person)

        return movie_crew
    except:
        return []
