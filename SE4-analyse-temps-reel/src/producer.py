import json
import time

with open("data/mock/stream_sample.json", "r") as f:
    data = json.load(f)
    for record in data:
        print("Envoi :", record)
        time.sleep(1)