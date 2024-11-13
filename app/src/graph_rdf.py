"""
Module de création d'un graphe RDF pour stocker les données d'une ontologie
"""

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

from conf import ontologie_schema_org, ontologie_schema_prefix

# Initialisation du graphe RDF
graph = Graph()

# Définition de l'ontologie
schema = Namespace(ontologie_schema_org)

# Liaison d'un préfixe à l'ontologie (pour passer de 'http://schema.org/Movie' à 'schema:Movie')
graph.bind(ontologie_schema_prefix, schema)

def get_rdf_graph():
    """
    Renvoyer le graphe RDF
    """
    return graph


def add_movies_from_json_api_to_rdf_graph(json_result_api):
    """
    Ajouter les films du fichier json au graphe RDF
    """

    if json_result_api["Response"] == "True":
        for movie in json_result_api["Search"]:
            add_movie_to_rdf_graph(movie)
    else:
        print("[ERREUR] Aucun film trouvé dans le fichier json reçu de l'API")


def add_movie_to_rdf_graph(movie):
    """
    Ajouter un film au graphe RDF
    """

    # Créer l'URI du film
    movie_uri = URIRef(f"http://projet-web-sem-cinema.org/movies/{movie['imdbID']}")

    # Ajouter le nom du film
    graph.add((movie_uri, schema.name, Literal(movie["Title"])))

    # Ajouter le type du film
    graph.add((movie_uri, RDF.type, schema.Movie))

    # Ajouter la date de sortie du film
    graph.add((movie_uri, schema.releaseDate, Literal(movie["Year"])))

    # Ajouter l'affiche du film
    graph.add((movie_uri, schema.image, Literal(movie["Poster"])))


def serialized_rdf_n_triples():
    """
    Sérialiser les triplets du graphe RDF en format N-Triples
    """
    return get_rdf_graph().serialize(format="nt")
