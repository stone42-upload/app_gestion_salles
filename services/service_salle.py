from data.dao_salle import DataSalle
class ServiceSalle:
    def __init__(self, dao_salle):
        self.dao_salle = dao_salle

    def ajouter_salle(self, salle):
        for donnee in (salle.code, salle.description, salle.categorie):
            if not donnee:
                print("Erreur: une donnée obligatoire est manquante." )
                return False

        if salle.capacite is None:
            print("Erreur : capacité manquante.")
            return False

        if salle.capacite < 1:
            print("Désolé une salle dont la capacité est inférieur à 1 ne peut pas être ajouter")
        else:
            self.dao_salle.insert_salle(salle)
            print("Cette salle a été correctement ajouter")
            return True

    def modifier_salle(self, salle):
        for donnee in (salle.code, salle.description, salle.categorie):
            if not donnee:
                print("Erreur: une donnée obligatoire est manquante." )
                return False

        if salle.capacite is None:
            print("Erreur : capacité manquante.")
            return False

        if salle.capacite < 1:
            print("capacité doit être supérieure ou égale à 1 pour modifier cette salle avec ces valeurs")
            return False
        else:
            self.dao_salle.update_salle(salle)
            print("Cette salle a été correctement modifiée")
            return True