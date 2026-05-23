# Architecture — SE1 Infrastructure & Mini-Cluster

## 1. Objectif

L’objectif de la sous-équipe SE1 est de mettre en place une infrastructure Big Data fonctionnelle permettant le stockage distribué des données avec Hadoop HDFS et le traitement distribué avec Apache Spark.

Le cluster est lancé avec Docker Compose afin de simuler une architecture distribuée sur une seule machine.

---

## 2. Framework choisi

Le framework choisi est :

- Hadoop HDFS pour le stockage distribué ;
- Apache Spark pour le traitement distribué.

## 3. Justification

Hadoop HDFS permet de stocker les données de manière distribuée à travers plusieurs DataNodes.

Apache Spark permet d’effectuer des traitements Big Data de manière rapide et distribuée.

Docker Compose permet de lancer facilement tous les services nécessaires sans installer Hadoop et Spark directement sur la machine.

---

## 4. Services Docker utilisés

| Service | Rôle |
|---|---|
| namenode | Gestion du système de fichiers HDFS |
| datanode1 | Stockage des blocs HDFS |
| datanode2 | Stockage des blocs HDFS |
| spark-master | Gestion du cluster Spark |
| spark-worker-1 | Exécution des tâches Spark |
| spark-worker-2 | Exécution des tâches Spark |

---

## 5. Ports utilisés

| Port | Service | Description |
|---|---|---|
| 9870 | Hadoop NameNode | Interface web HDFS |
| 9000 | Hadoop NameNode | Communication HDFS IPC |
| 8080 | Spark Master | Interface web Spark |
| 7077 | Spark Master | Communication Spark |
| 8081 | Spark Worker 1 | Interface web Worker 1 |
| 8082 | Spark Worker 2 | Interface web Worker 2 |

---

## 6. Remarque sur YARN

Dans cette version du mini-cluster, le traitement distribué est assuré par Apache Spark en mode standalone.

Le service ResourceManager YARN et le port 8088 ne sont pas utilisés dans cette configuration, car Spark fonctionne ici avec son propre master : `spark://spark-master:7077`.

---

## 7. Résultat

Le mini-cluster est fonctionnel :

- le NameNode Hadoop est actif ;
- les DataNodes sont actifs ;
- l’interface HDFS est accessible sur `http://127.0.0.1:9870` ;
- Spark Master est actif ;
- deux Spark Workers sont connectés ;
- un fichier CSV a été envoyé et lu depuis HDFS.
