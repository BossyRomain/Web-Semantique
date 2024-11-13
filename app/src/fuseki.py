"""
Module pour insérer les triplets RDF dans le triplestore
"""

from SPARQLWrapper import SPARQLWrapper, POST

from conf import fuseki_url

def insert_n_triples_data_in_triplestore(n_triples_data):
    """
    Insérer les triplets RDF dans le triplestore Fuseki
    """

    # Créer une requête SPARQL
    sparql_query = create_query(n_triples_data)

    try:
        sparql_query.query()
        print("[SUCCES] Les triplets RDF ont été ajoutés au triplestore")
    except Exception as e:
        print("[ERREUR] Impossible d'ajouter les triplets RDF au triplestore")


def create_query(n_triples_data):
    """
    Créer une requête SPARQL
    """

    sparql = SPARQLWrapper(fuseki_url)
    sparql.setMethod(POST)
    sparql.setQuery(f"""
    INSERT DATA {{
      {n_triples_data}
    }}
    """)
    return sparql
