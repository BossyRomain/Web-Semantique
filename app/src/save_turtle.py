"""
Module pour sauvegarder le graphe RDF dans un fichier Turtle
"""

from conf import type_data, page_nb, name_api

def save_turtle_rdf_graph(rdf_graph):
    """
    Sauvegarde les données du graphe RDF dans un fichier Turtle
    """

    # Définir le nom du fichier turtle
    turtle_file_name = "../files/turtle/" + name_api + "_" + type_data + "_page_" + str(page_nb) + ".ttl"

    # Sauvegarder le fichier turtle dans le dossier 'app/files/turtle'
    rdf_graph.serialize(turtle_file_name, format="turtle")
