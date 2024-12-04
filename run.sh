#!/bin/bash

cd app/src/

echo ""
echo "##########################################"
echo "#        Lancement du Projet ...         #"
echo "##########################################"
echo ""

echo "Nettoyage des fichiers générés ..."
echo ""
rm -f app/files/json/*
rm -f app/files/triples/*
rm -f app/files/turtle/*

echo "Lancement de l'application Python ..."
echo ""
python main.py

echo ""
echo "##########################################"
echo "#          Fin du Projet                 #"
echo "##########################################"
echo ""
