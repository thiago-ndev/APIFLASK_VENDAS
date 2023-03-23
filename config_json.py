import json
with open('credenciais.json') as arquivo_json:
    config = json.load(arquivo_json)
DATABASE_URL = config.get('DATABASE_URL')

