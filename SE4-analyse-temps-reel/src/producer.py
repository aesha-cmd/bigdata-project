# Producteur simulé — lit le fichier mock et envoie les données
import json
import time

with open("data/mock/stream_sample.json", "r") as f:
    for line in f:
        record = json.loads(line)
        print("Envoi :", record)
        time.sleep(1)