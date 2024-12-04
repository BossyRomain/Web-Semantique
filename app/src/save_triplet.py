"""
Module pour sauvegarder les triplet RDF dans un fichier
"""

from conf import type_data, page_nb, name_api

def save_triples_rdf_graph(n_triples_data):
    """
    Sauvegarde les données du graphe RDF dans un fichier N-Triples
    """

    # Définir le nom du fichier N-Triples
    triples_file_name = "../files/triples/" + name_api + "_" + type_data + "_page_" + str(page_nb) + ".nt"

    # Sauvegarder le fichier N-Triples dans le dossier 'app/files/triples'
    with open(triples_file_name, "w", encoding="utf-8") as file:
        file.write(n_triples_data)
