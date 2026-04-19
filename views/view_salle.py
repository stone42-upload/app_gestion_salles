import customtkinter as ctk
from models.salle import Salle

class ViewSalle(ctk.CTk):
    def __init__(self, service_salle):
        super().__init__()

        self.service_salle = service_salle

        self.title("Gestion des Salles")
        self.geometry("600x400")

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=20 ,padx=20, fill="x")

        champs = [
            ("Code :", "entry_code"),
            ("Description :", "entry_description"),
            ("Catégorie :", "entry_categorie"),
            ("Capacité :", "entry_capacite")
        ]

        for i, (label_text, entry_attr) in enumerate(champs):
            lbl = ctk.CTkLabel(self.frame_info, text=label_text)
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            entry = ctk.CTkEntry(self.frame_info)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)

        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        boutons = [
            ("Ajouter", "btn_ajouter"),
            ("Modifier", "btn_modifier"),
            ("Supprimer", "btn_supprimer"),
            ("Rechercher", "btn_rechercher")
        ]

        for col, (text, attr_name) in enumerate(boutons):
            btn = ctk.CTkButton(self.frame_actions, text=text)
            btn.grid(row=0, column=col, padx=10, pady=5)
            setattr(self, attr_name, btn)
        self.btn_ajouter.configure(command=self.ajouter_salle)
        self.btn_modifier.configure(command=self.modifier_salle)
        self.btn_supprimer.configure(command=self.supprimer_salle)

        for i in range(4):
            self.frame_actions.grid_columnconfigure(i, weight=1)


    def ajouter_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        try:
            capacite = int(capacite)
        except ValueError:
            print("Erreur : la capacité doit être un nombre entier")
            return

        salle = Salle(code, description, categorie, capacite)
        resultat = self.service_salle.ajouter_salle(salle)
        if resultat:
            print("La salle a été ajoutée avec succès")
        else:
            print("La salle n'a pas été ajouter")


    def modifier_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        try:
            capacite = int(capacite)
        except ValueError:
            print("Erreur : la capacité doit être un nombre entier")
            return

        salle = Salle(code, description, categorie, capacite)
        resultat = self.service_salle.modifier_salle(salle)

        if resultat:
            print("La salle a été modifier avec succes")
        else:
            print("La modification de la salle a échouer")


    def supprimer_salle(self):
        code = self.entry_code.get()

        resultat = self.service_salle.supprimer_salle(code)
        if resultat:
            print("La salle a supprimer avec succes")
        else:
            print("Impossible de supprimer la salle")