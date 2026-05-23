#!/bin/bash

echo "Création du dossier HDFS..."
hdfs dfs -mkdir -p /data/raw

echo "Upload du fichier sample.csv..."
hdfs dfs -put -f /data/sample.csv /data/raw/

echo "Liste des fichiers dans HDFS..."
hdfs dfs -ls /data/raw

echo "Lecture du fichier..."
hdfs dfs -cat /data/raw/sample.csv

echo "Test HDFS terminé avec succès."
