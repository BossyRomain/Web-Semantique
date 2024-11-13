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
ontologie_schema_org = "http://schema.org/"
ontologie_schema_prefix = "schema"

# Fuseki
fuseki_url = "http://localhost:3030/films/update"

######################
#      OMDB API      #
######################

name_api = "omdb"
omdb_api_key = "eaf9aada"
type_data = "movie"
key_word = "Harry"
page_nb = 1

# Rechercher les films à la "page" spécifiée avec "keyword" dans le titre
url_omdb_api = f"http://www.omdbapi.com/?apikey={omdb_api_key}&s={key_word}&page={page_nb}"
