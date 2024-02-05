import os
import json

DATA_FOLDER_PATH = "app/data"
GENRES = os.path.join(DATA_FOLDER_PATH, "genres.json")

with open(GENRES, 'r', encoding='utf-8') as json_file:
    genres = json.loads(json_file.read())
    
