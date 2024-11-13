import os
import json
import requests

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS
from SPARQLWrapper import SPARQLWrapper, POST

# Création des dossiers s'ils n'existent pas
os.makedirs("../json", exist_ok=True)
os.makedirs("../turtle", exist_ok=True)

# Configuration de l'API et du mot-clé
api_key = "eaf9aada"
keyword = "Harry"  # Mot-clé de recherche
url = f"http://www.omdbapi.com/?apikey={api_key}&s={keyword}&page=1"

# Récupération des données
response = requests.get(url)
data = response.json()

# Placer le fichier json dans le dossier app/json
with open("../json/films_page1.json", "w") as file:
    json.dump(data, file)

# Initialisation du graphe RDF
g = Graph()

# Choix de l'ontologie (ici : schema.org)
schema = Namespace("http://schema.org/")

# Conversion en triplets RDF
if data["Response"] == "True":
    for movie in data["Search"]:
        movie_uri = URIRef(f"http://film.org/films/{movie['imdbID']}")
        g.add((movie_uri, RDF.type, schema.Movie))
        g.add((movie_uri, schema.name, Literal(movie["Title"])))
        g.add((movie_uri, schema.releaseDate, Literal(movie["Year"])))
        g.add((movie_uri, schema.director, Literal(movie["Poster"])))

# Sauvegarder en format Turtle
g.serialize("../turtle/films_page1.ttl", format="turtle")

# Sérialiser les triplets en format N-Triples pour l'insertion SPARQL
triples_data = g.serialize(format="nt")

# Configuration de Fuseki
fuseki_url = "http://localhost:3030/films/update"

# Préparer la requête SPARQL pour insérer les triplets
sparql = SPARQLWrapper(fuseki_url)
sparql.setMethod(POST)
sparql.setQuery(f"""
INSERT DATA {{
  {triples_data}
}}
""")

# Exécuter la requête pour insérer les données
try:
    sparql.query()
    print("Triplets RDF ajoutés au triplestore avec succès.")
except Exception as e:
    print("Erreur lors de l'insertion des triplets RDF :", e)