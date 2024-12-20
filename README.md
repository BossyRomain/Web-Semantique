# Web-Semantique

Projet de web sémantique qui a pour but de créer une ontologie sur le thème du cinéma et de réaliser des requêtes SPARQL sur cette ontologie. Le projet est réalisé en Python et utilise le module `rdflib` pour manipuler les données RDF. Le serveur SPARQL utilisé est Apache Jena Fuseki. Le projet est réalisé dans le cadre du cours de web sémantique de l'Université de Grenoble.

## Fonctionnalités

Les fonctionnalités du projet sont les suivantes :

- Création d'une ontologie sur le thème du cinéma
- Création d'une base de données RDF
- Création de requêtes SPARQL

## Auteurs

- Romain BOSSY
- Adrien GLEMBA
- Troisème AUTEUR

## Architecture du projet

```plaintext
.
├── app
│   ├── json
│   │   └── cine-data.json
│   ├── src
│   │   └── main.py
│   └── turtle
│       └── cine-data.ttl
├── docs
│   ├── projet-Web-Sem-2024-2025.pdf
│   └── rapport.md
├── fuseki
│   └── apache-jena-fuseki-5.2.0
├── .gitignore
├── Backlog.md
├── README.md
├── run.sh
└── runServ.sh
```

## Technologies

Les technologies utilisées pour réaliser le projet sont les suivantes :

- `Python` pour le développement de l'application
- `rdflib` pour créer et manipuler le graphe RDF de l'ontologie
- `Namespace` pour définir le choix de l'ontologie
- `Apache Jena Fuseki` en tant que triplestore pour stocker les données RDF
- `SPARQL` pour affectuer des requêtes sur l'ontologie
- `SPARQLWrapper` pour exécuter des requêtes SPARQL en Python
- `JSON` pour récupérer les données depuis l'API
- `Turtle` pour récupérer le graphe RDF depuis le fichier JSON
- `N-Triples` pour stocker les données RDF dans le triplestore

## Prérequis

Pour utiliser le projet, il faut installer les dépendances suivantes :

```bash
- Python
```

## Installation

Pour installer le projet, il suffit de cloner le dépôt git et de lancer le serveur python.

```bash
> git clone https://github.com/BossyRomain/Web-Semantique.git
```

## Utilisation

Pour utiliser le projet, il faut exécuter le serveur Apache Jena Fuseki et l'application Python.

### 1 - Exécuter le server Apache Jena Fuseki

- Pour exécuter le serveur Apache Jena Fuseki, il faut ouvrir un terminal et se placer à la racine du projet.
- Ensuite, il faut exécuter le script `runServ.sh` :

```bash
> ./runServ.sh
```

### 2 - Exécuter l'application Python

- Pour exécuter l'application Python, il faut ouvrir un autre terminal et se placer à la racine du projet.
- Ensuite, il faut exécuter le script `run.sh` :

```bash
> ./run.sh
```

### 3 - Utiliser l'application

> Pour utiliser l'application, il suffit de suivre les instructions affichées dans le terminal.

```bash
> To Do
```

## Ontologie

L'ontologie est disponible dans le fichier `ontology.owl`.

## Requêtes

Les requêtes sont disponibles dans le fichier `queries.rq`.

## Résultats

Les résultats des requêtes sont disponibles dans le fichier `results.txt`.
