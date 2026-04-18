from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()
# Test de la connection à la base de données
conn = dao.get_connect()

s1 = Salle("A101", "Salle informatique", "Informatique", 30)
s2 = Salle("B302", "Salle de conférence", "Réunion", 500)
# Ajout d'une salle à la base de donnée
dao.insert_salle(s1)
dao.insert_salle(s2)
# Suppression d'une salle dans la base de donnée
dao.delete_salle("B302")

# Modification de la salle ("A101")
s1.description = "Salle de cours"
dao.update_salle(s1)

#Recherche d'une salle par son code
dao.get_salle("B302")
# Récupération et affichage de toutes les salles
print(dao.get_salles())







