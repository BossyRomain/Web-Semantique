import os
import json
import requests

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS

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
schema = Namespace("http://schema.org/")

# Conversion en triplets RDF
if data["Response"] == "True":
    for movie in data["Search"]:
        movie_uri = URIRef(f"http://cyber_film.org/films/{movie['imdbID']}")
        g.add((movie_uri, RDF.type, schema.Movie))
        g.add((movie_uri, schema.name, Literal(movie["Title"])))
        g.add((movie_uri, schema.releaseDate, Literal(movie["Year"])))
        g.add((movie_uri, schema.director, Literal(movie["Poster"])))

# Sauvegarder en format Turtle
g.serialize("../turtle/films_page1.ttl", format="turtle")
