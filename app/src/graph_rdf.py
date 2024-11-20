"""
Module de création d'un graphe RDF pour stocker les données d'une ontologie
"""

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

from conf import ontologie_schema_org_movie, ontologie_schema_prefix_movie, ontologie_schema_org_creative_work, ontologie_schema_prefix_creative_work, ontologie_schema_org_thing, ontologie_schema_prefix_thing

# Initialisation du graphe RDF
graph = Graph()

# Définition des ontologies
schema_movie = Namespace(ontologie_schema_org_movie)
schema_creative_work = Namespace(ontologie_schema_org_creative_work)
schema_thing = Namespace(ontologie_schema_org_thing)

# Liaison des préfixes aux ontologies (pour passer de 'http://schema.org/Movie/' à 'schema-movie')
graph.bind(ontologie_schema_prefix_movie, schema_movie)
graph.bind(ontologie_schema_prefix_creative_work, schema_creative_work)
graph.bind(ontologie_schema_prefix_thing, schema_thing)

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
    graph.add((movie_uri, schema_thing.name, Literal(movie["Title"])))

    # Ajouter la date de sortie du film
    graph.add((movie_uri, schema_creative_work.datePublished, Literal(movie["Year"])))

    # Ajouter l'affiche du film
    graph.add((movie_uri, schema_creative_work.thumbnailUrl, Literal(movie["Poster"])))


def serialized_rdf_n_triples():
    """
    Sérialiser les triplets du graphe RDF en format N-Triples
    """
    return get_rdf_graph().serialize(format="nt")
