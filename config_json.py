import json
with open('credenciais.json.txt') as arquivo_json:
    config = json.load(arquivo_json)
DATABASE_URL = config.get('DATABASE_URL')

