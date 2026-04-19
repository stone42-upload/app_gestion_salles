import json
import mysql.connector

from models.salle import Salle


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

    def insert_salle(self, salle):
        conn = self.get_connect()
        crs = conn.cursor()
        crs.execute("""
        CREATE TABLE IF NOT EXISTS salle (
            code VARCHAR(5) PRIMARY KEY,
            description VARCHAR(50),
            categorie VARCHAR(50),
            capacite INT
            )"""
        )
        conn.commit()

        crs.execute("INSERT INTO salle (code, description, categorie, capacite)" 
                    "VALUES (%s, %s, %s, %s)",
                    (salle.code, salle.description, salle.categorie, salle.capacite))
        conn.commit()

        print("Cette salle a été insérer correctement")
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connect()
        crs = conn.cursor()
        crs.execute("""
            UPDATE salle
            SET  description = %s, categorie = %s, capacite = %s
            WHERE code = %s
        """, (salle.description, salle.categorie, salle.capacite, salle.code))

        conn.commit()
        conn.close()

    def delete_salle(self, code):
       conn = self.get_connect()
       crs = conn.cursor()
       crs.execute("DELETE FROM salle WHERE code = %s", (code,))
       conn.commit()

       print("La salle a été supprimer correctement ")
       conn.close()

    def get_salle(self, code):
        conn = self.get_connect()
        crs = conn.cursor()
        crs.execute("SELECT * FROM salle WHERE code = %s", (code,))
        salle = crs.fetchone()
        conn.close()
        return salle

    def get_salles(self):
        conn = self.get_connect()
        crs = conn.cursor()
        crs.execute("SELECT * FROM salle")
        rows = crs.fetchall()
        salles = []
        for row in rows:
            code, description, categorie, capacite = row
            salles.append(Salle(code, description, categorie, capacite))

        conn.close()
        return salles

