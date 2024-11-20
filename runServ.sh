#!/bin/bash

# Executer le serveur Fuseki
cd fuseki/apache-jena-fuseki-5.2.0/
./fuseki-server

# Affichage console
echo ""
echo "######################################################"
echo "# L'application est lancée sur http://localhost:3030 #"
echo "######################################################"
echo ""