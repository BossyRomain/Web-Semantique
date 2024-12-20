# Rapport de projet Web-Sémantique

## Domaine d'application

Le domaine d'application choisi pour ce projet est la gestion de `Films`. Ce domaine a été choisi, car il est riche en données et en informations. Il est possible de récupérer des informations sur les films telles que le titre, la date de sortie, l'affiche, le réalisateur, les acteurs, les producteurs, etc. De plus, il est possible de récupérer des informations sur les personnes qui ont participé au film comme les acteurs, les réalisateurs, les producteurs avec leur nom, la date de naissance, etc.

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

1. Concevoir une Ontologie
• Créer ou réutiliser une ontologie adaptée à votre domaine. Une ontologie définit les
concepts et les relations dans un domaine donné, ce qui permet de donner du sens à
vos données.
• Utiliser des vocabulaires existants lorsque possible (comme FOAF, Dublin Core, ou
Schema.org) pour garantir l'interopérabilité.
• Création d’une ontologie : Si aucune ontologie ne convient, vous devrez en créer
une, par exemple en utilisant Protégé, un outil de conception d'ontologies.
• Outils utiles pour créer des ontologies : Protégé,  
