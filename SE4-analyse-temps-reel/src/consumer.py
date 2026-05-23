import json

records = []

with open("data/mock/stream_sample.json", "r") as f:
    data = json.load(f)
    for record in data:
        records.append(record["valeur"])
        moyenne = sum(records) / len(records)
        print(f"Reçu : {record['valeur']} | Moyenne : {moyenne:.2f}")