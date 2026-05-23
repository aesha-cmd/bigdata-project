# Projet Big Data — Groupe 4

## SE1 — Infrastructure & Mini-Cluster

### 1. Objectif

Cette partie du projet correspond à la sous-équipe SE1 : Infrastructure & Mini-Cluster.

L’objectif est de mettre en place un mini-cluster Big Data permettant :

- le stockage distribué des données avec Hadoop HDFS ;
- le traitement distribué avec Apache Spark ;
- la préparation d’un environnement commun pour les autres sous-équipes du projet.

Ce mini-cluster est exécuté avec Docker Compose sur une seule machine, mais il simule une architecture distribuée.

---

### 2. Technologies utilisées

- Docker Desktop
- Docker Compose
- Apache Hadoop 3.3.6
- Hadoop HDFS
- Apache Spark 3.5.1

---

### 3. Architecture du mini-cluster

Le cluster contient :

- 1 NameNode Hadoop
- 2 DataNodes Hadoop
- 1 Spark Master
- 2 Spark Workers

Architecture simplifiée :

```text
Utilisateur
   |
   v
Docker Compose
   |
   +--> Hadoop NameNode : namenode:9000 / Web UI : 9870
   |
   +--> Hadoop DataNode 1
   |
   +--> Hadoop DataNode 2
   |
   +--> Spark Master : spark://spark-master:7077 / Web UI : 8080
   |
   +--> Spark Worker 1
   |
   +--> Spark Worker 2
```

---

### 4. Structure du projet

```text
SE1_infrastructure/
├── docker-compose.yml
├── README.md
├── architecture.md
├── config/
│   ├── core-site.xml
│   └── hdfs-site.xml
├── data/
│   └── sample.csv
├── scripts/
│   └── test_hdfs.sh
└── screenshots/
    ├── 01_docker_ps.png
    ├── 02_hadoop_namenode.png
    ├── 03_spark_master.png
    └── 04_hdfs_test.png
```

---

### 5. Prérequis

Avant de lancer le projet, il faut installer :

- Docker Desktop
- Git, si le projet est récupéré depuis GitHub

Vérification de Docker :

```bash
docker --version
```

Vérification de Docker Compose :

```bash
docker compose version
```

---

### 6. Lancement du mini-cluster

Depuis le dossier du projet :

```bash
docker compose up -d
```

Cette commande lance automatiquement :

- Hadoop NameNode
- Hadoop DataNode 1
- Hadoop DataNode 2
- Spark Master
- Spark Worker 1
- Spark Worker 2

---

### 7. Vérification des conteneurs

Pour vérifier que les services sont actifs :

```bash
docker ps
```

Résultat attendu :

```text
namenode        Up
datanode1       Up
datanode2       Up
spark-master    Up
spark-worker-1  Up
spark-worker-2  Up
```

---

### 8. Interface Hadoop NameNode

L’interface web Hadoop est disponible ici :

```text
http://127.0.0.1:9870
```

Cette interface permet de vérifier l’état du NameNode, des DataNodes et du système HDFS.

---

### 9. Interface Spark Master

L’interface web Spark est disponible ici :

```text
http://127.0.0.1:8080
```

Elle permet de vérifier le Spark Master, les Spark Workers actifs, les ressources CPU/mémoire et les applications Spark exécutées.

---

### 10. Test HDFS

Entrer dans le conteneur NameNode :

```bash
docker exec -it namenode bash
```

Créer un dossier dans HDFS :

```bash
hdfs dfs -mkdir -p /data/raw
```

Envoyer le fichier `sample.csv` vers HDFS :

```bash
hdfs dfs -put -f /data/sample.csv /data/raw/
```

Lister les fichiers dans HDFS :

```bash
hdfs dfs -ls /data/raw
```

Lire le fichier depuis HDFS :

```bash
hdfs dfs -cat /data/raw/sample.csv
```

Résultat attendu :

```text
Found 1 items
/data/raw/sample.csv

id,user,event,timestamp
1,aicha,click,29/04/2026 10:00
2,hajar,view,29/04/2026 10:01
3,yassine,purchase,29/04/2026 10:02
4,sara,click,29/04/2026 10:03
5,amine,view,29/04/2026 10:04
```

---

### 11. Arrêt du cluster

Pour arrêter les conteneurs sans supprimer les volumes :

```bash
docker compose down
```

Pour arrêter le cluster et supprimer les volumes HDFS :

```bash
docker compose down -v
```

Attention : `docker compose down -v` supprime les données stockées dans les volumes Docker.

---

### 12. Livrables SE1

Les livrables de la sous-équipe SE1 sont :

- un mini-cluster fonctionnel ;
- un fichier `docker-compose.yml` ;
- les fichiers de configuration Hadoop ;
- un fichier `README.md` ;
- un fichier `architecture.md` ;
- des captures d’écran de preuve ;
- un test HDFS fonctionnel.

Captures disponibles :

```text
01_docker_ps.png
02_hadoop_namenode.png
03_spark_master.png
04_hdfs_test.png
```

---

### 13. Conclusion

La sous-équipe SE1 a préparé l’infrastructure Big Data du projet.

Le mini-cluster est fonctionnel :

- Hadoop HDFS est actif ;
- le NameNode est accessible ;
- les DataNodes sont connectés ;
- Spark Master est actif ;
- deux Spark Workers sont connectés ;
- un fichier CSV a été envoyé et lu depuis HDFS.

Cette infrastructure peut maintenant être utilisée par les autres sous-équipes pour l’ingestion, le traitement ETL, l’analyse temps réel et la visualisation.
