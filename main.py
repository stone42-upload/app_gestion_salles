from models.salle import Salle
from services.service_salle import ServiceSalle
from data.dao_salle import DataSalle
dao = DataSalle()
service = ServiceSalle(dao)

print(service.recuperer_salles())

s3 = Salle("D154", "Salle de cours première année", "Cours",80)
service.ajouter_salle(s3)

s3.capacite=70
service.modifier_salle(s3)

service.supprimer_salle("D154")

print(service.rechercher_salle("A101"))