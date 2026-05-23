#!/bin/bash

mkdir -p SE1-infrastructure/config SE1-infrastructure/scripts
mkdir -p SE2-ingestion/data/mock SE2-ingestion/src SE2-ingestion/tests
mkdir -p SE3-traitement-etl/src SE3-traitement-etl/tests
mkdir -p SE4-analyse-temps-reel/src SE4-analyse-temps-reel/config SE4-analyse-temps-reel/data/mock SE4-analyse-temps-reel/tests
mkdir -p SE5-visualisation/src SE5-visualisation/dashboard SE5-visualisation/rapport

touch SE1-infrastructure/README.md SE1-infrastructure/architecture.md SE1-infrastructure/docker-compose.yml
touch SE1-infrastructure/config/core-site.xml SE1-infrastructure/config/hdfs-site.xml SE1-infrastructure/config/yarn-site.xml
touch SE1-infrastructure/scripts/start-cluster.sh SE1-infrastructure/scripts/test-cluster.sh

touch SE2-ingestion/README.md SE2-ingestion/dataset.md
touch SE2-ingestion/src/ingestion.py SE2-ingestion/src/validator.py
touch SE2-ingestion/tests/test_ingestion.py

touch SE3-traitement-etl/README.md SE3-traitement-etl/transformations.md
touch SE3-traitement-etl/src/etl_pipeline.py SE3-traitement-etl/src/transformations.py
touch SE3-traitement-etl/tests/test_etl.py

touch SE4-analyse-temps-reel/README.md SE4-analyse-temps-reel/choix-technologie.md
touch SE4-analyse-temps-reel/src/producer.py SE4-analyse-temps-reel/src/consumer.py SE4-analyse-temps-reel/src/aggregations.py
touch SE4-analyse-temps-reel/tests/test_streaming.py

touch SE5-visualisation/README.md SE5-visualisation/choix-outil.md SE5-visualisation/kpis.md
touch SE5-visualisation/src/app.py SE5-visualisation/src/data_connector.py

touch SUIVI.md

echo "Structure creee avec succes !"
