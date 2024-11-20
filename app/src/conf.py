"""
Module de configuration de l'application
"""

import os

# Créer les dossiers 'json' et 'turtle' s'ils n'existent pas
os.makedirs("../files", exist_ok=True)
os.makedirs("../files/json", exist_ok=True)
os.makedirs("../files/turtle", exist_ok=True)

######################
#    CONFIGURATION   #
######################

# Ontologie
ontologie_schema_org_movie = "https://schema.org/Movie/"
ontologie_schema_prefix_movie = "schema-movie"

ontologie_schema_org_creative_work = "https://schema.org/CreativeWork/"
ontologie_schema_prefix_creative_work = "schema-creative-work"

ontologie_schema_org_thing = "https://schema.org/Thing/"
ontologie_schema_prefix_thing = "schema-thing"

onthologie_schema_org_person = "https://schema.org/Person"
onthologie_schema_prefix_person = "schema-person"

# Fuseki
fuseki_url = "http://localhost:3030/movies/update"

######################
#      OMDB API      #
######################

name_api = "omdb"
omdb_api_key = "eaf9aada"
type_data = "movie"
key_word = "Harry"
page_nb = 2

# Rechercher les films à la "page" spécifiée avec "keyword" dans le titre
url_omdb_api = f"http://www.omdbapi.com/?apikey={omdb_api_key}&s={key_word}&page={page_nb}"

######################
#  The Movie DB API  #
######################

themovedb_api_key = "cc3adef3826285c96e65cbd79fffa82e"

# Rechercher les personnes qui ont travaillé sur le film
url_themoviedb_api = f'https://api.themoviedb.org/3/'