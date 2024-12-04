"""
Module pour sauvegarder les données reçues de l'API dans un fichier json
"""

import json

from conf import type_data, page_nb, name_api

def save_json_data(response_api):
    """
    Renvoi et sauvegarde les données reçues d'une API dans un fichier json
    """

    # Convertir les données en format json
    json_data_api = response_api.json()

    # Définir le nom du fichier json
    json_file_name = "../files/json/" + name_api + "_" + type_data + "_page_" + str(page_nb) + ".json"

    # Sauvegarder le fichier json dans le dossier 'app/files/json'
    with open(json_file_name, "w", encoding="utf-8") as file:
        json.dump(json_data_api, file)

    return json_data_api
