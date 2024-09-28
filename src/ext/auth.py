from flask_jwt_extended import JWTManager
from src.blacklist import BLACKLIST
from src import blacklist
from flask import jsonify

def init_app(app):
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def verificar_blacklist(jwt_header, jwt_payload: dict):
        jti = jwt_payload['jti']
        print('JTI VERIFICADA: ' + jti)
        print(BLACKLIST)
        return jti in BLACKLIST

    @jwt.revoked_token_loader
    def token_invalido(jwt_header, jwt_payload: dict):
        print('DENTRO DO REVOKED TOKEN')
        print(blacklist.BLACKLIST)
        return jsonify({'mensage': 'token invalidado'})