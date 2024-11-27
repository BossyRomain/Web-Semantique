"""
Module de création d'un graphe RDF pour stocker les données d'une ontologie
"""

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

from conf import ontologie_schema_org_movie, ontologie_schema_prefix_movie, ontologie_schema_org_creative_work, ontologie_schema_prefix_creative_work, ontologie_schema_org_thing, ontologie_schema_prefix_thing, url_themoviedb_api, onthologie_schema_org_person, onthologie_schema_prefix_person
from api import get_movie_crew

# Initialisation du graphe RDF
graph = Graph()

# Définition des ontologies
schema_movie = Namespace(ontologie_schema_org_movie)
schema_creative_work = Namespace(ontologie_schema_org_creative_work)
schema_thing = Namespace(ontologie_schema_org_thing)
schema_person = Namespace(onthologie_schema_org_person)

# Liaison des préfixes aux ontologies (pour passer de 'http://schema.org/Movie/' à 'schema-movie')
graph.bind(ontologie_schema_prefix_movie, schema_movie)
graph.bind(ontologie_schema_prefix_creative_work, schema_creative_work)
graph.bind(ontologie_schema_prefix_thing, schema_thing)
graph.bind(onthologie_schema_prefix_person, schema_person)

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


def add_movies_crews_from_json_api_to_rdf_graph(json_result_api):
    """
    Ajoute les membres des équipes des films dans le graphe RDF
    """
    if json_result_api["Response"] == "True":
        for movie in json_result_api["Search"]:
            crew = get_movie_crew(movie)
            add_crew_to_rdf(crew, movie["imdbID"])
    else:
        print("[ERREUR] Aucun film trouvé dans le fichier json reçu de l'API")


def add_crew_to_rdf(crew, movie_imdb_id):
    """
    Ajoute les membres de l'équipe d'un film dans le graphe RDF
    """
    for person in crew:
        # Ajout d'un membre'
        add_person_to_rdf(person)

        # Ajout du rôle du membre pour le film
        movie_uri = URIRef(f"http://projet-web-sem-cinema.org/movies/{movie_imdb_id}")

        person_uri = URIRef(f"{url_themoviedb_api}/person/{person['id']}")

        match person['job']:
            case "actor":
                graph.add((movie_uri, schema_movie.actor, person_uri))

            case "director":
                graph.add((movie_uri, schema_movie.director, person_uri))
            
            case "producer":
                graph.add((movie_uri, schema_movie.producer, person_uri))
            
            case "editor":
                graph.add((movie_uri, schema_movie.editor, person_uri))
        



def add_person_to_rdf(person):
    """
    Ajoute une personne dans le graphe RDF
    """
    person_uri = URIRef(f"{url_themoviedb_api}/person/{person['id']}")

    graph.add((person_uri, schema_person.name, Literal(person['name'])))

    graph.add((person_uri, schema_person.birthDate, Literal(person['birthday'])))

    graph.add((person_uri, schema_person.birthPlace, Literal(person['place_of_birth'])))


def serialized_rdf_n_triples():
    """
    Sérialiser les triplets du graphe RDF en format N-Triples
    """
    return get_rdf_graph().serialize(format="nt")
