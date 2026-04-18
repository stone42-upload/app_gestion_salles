import json
import mysql.connector

class  DataSalle:

    def get_connect(self):
        with open("data/config.json") as f:
            data = json.load(f)

        connexion = mysql.connector.connect(
            host=data['host'],
            user=data['user'],
            password=data['password'],
            database=data['database']
        )
        return connexion

