"""
Programme principal de l'application.

Ce programme permet de :
- Récupérer les données de l'API OMDB,
- Les sauvegarder dans un fichier JSON,
- Les ajouter à un graphe RDF,
- Sauvegarder ce graphe dans un fichier Turtle,
- Sérialiser les triplets en format N-Triples,
- Les insérer dans un triplestore Fuseki.
"""

import requests

from graph_rdf import add_movies_from_json_api_to_rdf_graph, get_rdf_graph, serialized_rdf_n_triples
from fuseki import insert_n_triples_data_in_triplestore
from save_turtle import save_turtle_rdf_graph
from save_json import save_json_data
from conf import url_omdb_api

######################
#      OMDB API      #
######################

# Récupérer les données de l'API OMDB
response_omdb_api = requests.get(url_omdb_api)

######################
#      JSON FILE     #
######################

# Sauvegarder les données dans un fichier json
json_result_api = save_json_data(response_omdb_api)

######################
#      GRAPH RDF     #
######################

# Ajouter les films du fichier json au graphe RDF
add_movies_from_json_api_to_rdf_graph(json_result_api)

######################
#     TURTLE FILE    #
######################

# Sauvegarder le graphe RDF dans un fichier Turtle
save_turtle_rdf_graph(get_rdf_graph())

######################
#    N-TRIPLES RDF   #
######################

# Sérialiser les triplets en format N-Triples
n_triples_data = serialized_rdf_n_triples()

######################
#       FUSEKI       #
######################

# Insérer les triplets RDF dans le triplestore Fuseki
insert_n_triples_data_in_triplestore(n_triples_data)
