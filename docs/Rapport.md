# Rapport de projet Web-Sémantique

Projet de web sémantique réalisé dans le cadre du cours de web sémantique de l'Université de Grenoble.

## Domaine d'application

Le domaine d'application choisi pour ce projet est la gestion de `Films`. Ce domaine a été choisi, car il est riche en données et en informations. Il est possible de récupérer des informations sur les films telles que le titre, la date de sortie, l'affiche, le réalisateur, les acteurs, les producteurs, etc. De plus, il est possible de récupérer des informations sur les personnes qui ont participé au film comme les acteurs, les réalisateurs, les producteurs avec leur nom, la date de naissance, etc.

## Auteurs

- Romain BOSSY
- Adrien GLEMBA
- Fatima Zahra Roudani

## Objectifs du projet

Les objectifs du projet sont les suivants :

- Récupérer des données sur des films depuis une ou plusieurs `API`
- Créer une `Ontologie` sur le thème du cinéma
- Créer un `Graphe RDF` à partir des données récupérées
- Choisir un `Triple Store`
- Stocker le `Graphe RDF` dans le `Triple Store` choisi
- Réaliser des `Requêtes SPARQL` sur le `Triple Store` permettant de :
  - Afficher tous les films stockés
  - Afficher le nombre de films stockés
  - Retourner les acteurs d'un film
  - Retourner les films d'un réalisateur
  - Retourner les réalisateurs d'un film
  - Rechercher un film par son titre
  - Trier les films par date de sortie décroissante

## Choix des données

L'avantage de passer par des `API` est que nous pouvons récupérer des données sur les films de manière structurée et organisée. Les `API` fournissent des données sur les films sous forme de `JSON` ou `XML` qui sont faciles à manipuler et à traiter. De plus, les `API` fournissent des informations sur les films qui sont à jour et précises. Nous avons récupérer des données depuis deux `API` différentes :

- `OMDB API` : API qui fournit des informations sur les films. Nous avons récupéré des informations sur les films telles que le titre, la date de sortie, l'affiche, l'identifiant IMDB, etc.

- `The Movie Database (TMDb)` : API qui fournit d'autres informations sur les films. Nous avons récupéré des informations sur les films telles que le réalisateur, les acteurs, les producteurs, etc.

## Comprendre et préparer les Données

### Conceptes et variables

- `Film` : Un film est une oeuvre cinématographique qui est réalisée par un réalisateur et qui met en scène des acteurs. Un film a un titre, une date de sortie, une affiche, un réalisateur, des acteurs, des producteurs, etc.

- `Personne` : Une personne est un individu qui peut être un acteur, un réalisateur, un producteur, etc. Une personne a un nom, une date de naissance, un lieu de naissance, etc.

### Relations entre concepts

- `Film` et `Personne` : Un film est réalisé par un réalisateur et met en scène des acteurs. Un film a un réalisateur et des acteurs. Un acteur joue dans un film et un réalisateur réalise un film.

### Nettoyage et préparation des données

- Les données récupérées depuis les `API` sont déjà bien structurées et organisées. Nous avons juste besoin de les traiter et de les transformer en `RDF` pour les stocker dans le `Triple Store`.
- L'uniformisation des données entre les deux `API` a été faite pour faciliter la manipulation des données grâce aux identifiants `IMDB` présents dans les deux `API`.

## Ontologie

Nous avons choisi d'utiliser l'ontologie suivante :

- `Shema.org` : Une ontologie qui fournit un cadre standardisé permettant de structurer et de baliser des données sur le web. Elle facilite l'interopérabilité avec d'autres systèmes ou données déjà structurées sur le web. Elle a été développée conjointement par les grands moteurs de recherche comme Google, Bing, Yahoo et Yandex.

Plus précisément, nous avons utilisé les classes de `Shema.org` suivantes :

- `Thing` : Pour nommer un objet :
  - `name` : Utilisé pour nommer un `Film` et une `Personne`
- `CreativeWork` : Pour représenter des informations sur une oeuvre créative _(ici un Movie)_ :
  - `datePublished` : Date de publication de l'oeuvre
  - `thumbnailUrl` : URL vers l'image de l'oeuvre
- `Movie` : Pour représenter des informations sur un film :
  - `actor` : Acteur jouant dans le film
  - `director` : Réalisateur du film
  - `producer` : Producteur du film
  - `editor` : Monteur du film
- `Person` : Pour représenter une personne grâce à ses attributs :
  - `birthDate` : Date de naissance de la personne
  - `birthPlace` : Lieu de naissance de la personne

Note : Il est important de noter que l'ontologie `Movie` est une sous-classe de `CreativeWork` et que `CreativeWork` et `Person` sont des sous-classes de `Thing`.

## Technologies utilisées

### Python

Nous avons utilisé le langage de programmation `Python` pour réaliser ce projet car il est facile à apprendre et à utiliser. De plus, c'est un langage peu verbeux et très lisible qui possède de nombreuses librairies et modules qui facilitent la manipulation des données. `Python` est un langage de programmation interprété, orienté objet et de haut niveau qui possède une grande communauté de développeurs qui partagent leurs connaissances et leurs expériences.

### JSON

Nous avons utilisé le format de données `JSON` pour stocker les données récupérées depuis les `API`. `JSON` est un format de données textuelles qui est facile à lire et à écrire pour les humains et facile à analyser et à générer pour les machines. `JSON` est un format de données très utilisé pour échanger des données entre des applications et des services web. De plus, il est très facile à manipuler en `Python`.

### Turtle

Nous avons utilisé le format de données `Turtle` pour stocker les données RDF dans des fichiers. `Turtle` est un format de données textuelles qui permet de représenter des triplets RDF de manière lisible et compréhensible. `Turtle` est un format de données très utilisé pour stocker des données RDF dans des fichiers.

### N-Triples

Nous avons utilisé le format de données `N-Triples` pour stocker les données RDF dans le `Triple Store`. `N-Triples` est un format de données textuelles qui permet de représenter des triplets RDF de manière simple et efficace.

### RDFLib

Nous avons utilisé la librairie `rdflib` pour manipuler les données RDF. `rdflib` est une librairie `Python` qui permet de créer des graphes RDF, de les stocker dans des fichiers, de les charger depuis des fichiers, de les afficher, de les modifier, etc.

### SPARQLWrapper

Nous avons utilisé la librairie `SPARQLWrapper` pour réaliser des requêtes `SPARQL` sur le `Triple Store`. `SPARQLWrapper` est une librairie `Python` qui permet d'exécuter des requêtes `SPARQL` sur un serveur `SPARQL` et de récupérer les résultats de ces requêtes.

## Triple Store

Nous avons choisi d'utiliser le `Triple Store` `Fuseki` _(Apache Jena Fuseki)_, car il est facile à installer, grâce à un serveur `Apache`, et à utiliser, via son interface web. De plus, il peut être utilisé dans un projet `Python` afin d'y stocker automatiquement des données grâce à la librairie `rdflib`. Enfin, il est possible de réaliser des requêtes `SPARQL` sur le `Triple Store` via l'interface web de `Fuseki`.

Note : Nous avons aussi essayé d'utiliser le `Triple Store` `GraphDB`, car ce dernier renvoi de meilleurs messages d'erreurs que `Fuseki` et il propose une interface web plus intuitive permettant de visualiser le graphe RDF stocké. Cependant, une fois le problème résolu, nous avons préféré ré-utiliser `Fuseki`, car le projet était finalement opérationnel.

## Requtes SPARQL

Nous avons réalisé des requêtes `SPARQL` qui réalisent les opérations suivantes :

- Afficher tous les films stockés _(Les entités de la classe `Movie`)_
- Afficher le nombre de films stockés _(Le nombre d'entités de la classe `Movie`)_
- Retourner les acteurs d'un film _(La relation entre un film et un acteur)_
- Retourner les films d'un réalisateur _(La relation entre un film et un réalisateur)_
- Retourner les réalisateurs d'un film _(La relation entre un film et un réalisateur)_
- Rechercher un film par son titre _(recherche une entité de la classe `Movie` avec un titre donné)_
- Trier les films par date de sortie décroissante _(Trie les entités de la classe `Movie` par date de sortie décroissante)_

## Architecture du projet

```plaintext
.
├── app
│   ├── files
│   │   ├── json
│   │   │   └── omdb_movie_page_1.json
│   │   ├── sparql
│   │   │   ├── afficher_tous_les_films.rq
│   │   │   └── ...
│   │   └── triples
│   │   │   └── omdb_movie_page_1.nt
│   │   └── turtle
│   │       └── omdb_movie_page_1.ttl
│   └── src
│       ├── main.py
│       └── ...
├── docs
│   ├── projet-Web-Sem-2024-2025.pdf
│   └── Rapport.md
├── fuseki
│   └── apache-jena-fuseki-5.2.0
├── .gitignore
├── Backlog.md
├── README.md
├── requirements.txt
├── run.sh
└── runServ.sh
```

## Utilisation de l'application

## Prérequis

Pour utiliser le projet, il faut installer les dépendances suivantes :

```bash
- Python
```

## Installation

Pour installer le projet, il suffit de cloner le dépôt git :

```bash
> git clone https://github.com/BossyRomain/Web-Semantique.git
```

Ensuite, il faut installer les dépendances du projet qui sont listées dans le fichier `requirments.txt` :

```bash
> cd Web-Semantique
> pip install -r requirements.txt
```

## Utilisation

Pour utiliser le projet, il faut exécuter le serveur Apache Jena Fuseki _(script `runServ.sh`)_ et l'application Python _(script `run.sh`)_ :

```bash
> cd Web-Semantique
> ./runServ.sh (dans un terminal)
> ./run.sh (dans un autre terminal)
```

Ensuite, il faut ouvrir un navigateur web et accéder à l'adresse suivante pour visualiser le graphe RDF stocké dans le Triple Store :

```bash
http://localhost:3030/#/
```

Puis pour accéder à l'interface web de `Fuseki` pour réaliser des requêtes `SPARQL`, il faut cliquer sur le bouton `Query` de votre dataset `movies`.

Enfin, éditter le champ de texte pour écrire une requête `SPARQL` et cliquer sur le bouton `Run` _(ou cliquer sur la `Flèche d'exécution`)_ pour exécuter la requête et afficher les résultats.

Si le terminal dans lequel vous avez lancé le script `run.sh` affiche le message suivant :

```bash
[SUCCES] Les triplets RDF ont été ajoutés au triplestore

##########################################
#          Fin du Projet                 #
##########################################
```

Cela signifie que le projet a été correctement exécuté et que les données ont été stockées dans le `Triple Store`.

Tips : Si ce n'est pas déjà fait, il faut créer un nouveau dataset une fois sur l'interface web de `Fuseki` _(nommé `movies` par exemple)_ sinon le script du projet _(`run.sh`)_ ne pourra pas stocker les données dans le `Triple Store`.

## Conclusion

Ce projet nous a permis de découvrir le monde du web sémantique et de manipuler des données structurées et organisées. Nous avons pu récupérer des données sur des films depuis des `API`, créer une `Ontologie` sur le thème du cinéma, créer un `Graphe RDF` à partir des données récupérées, stocker le `Graphe RDF` dans un `Triple Store`, et réaliser des `Requêtes SPARQL` sur le `Triple Store`. Nous avons pu mettre en pratique les concepts vus en cours et en travaux pratiques. Nous avons pu aussi découvrir des outils et des technologies comme `Fuseki`, `GraphDB`, `rdflib`, `SPARQL`, etc qui sont utilisés dans le domaine du web sémantique. Enfin, nous avons pu réaliser un projet complet et fonctionnel qui répond aux objectifs fixés.
