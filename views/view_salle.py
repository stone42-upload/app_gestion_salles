import customtkinter as ctk
from models.salle import Salle
from tkinter import ttk

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
        self.btn_rechercher.configure(command=self.rechercher_salle)

        for i in range(4):
            self.frame_actions.grid_columnconfigure(i, weight=1)

        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
        self.lister_salles()

    def ajouter_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        salle = Salle(code, description, categorie, capacite)
        resultat = self.service_salle.ajouter_salle(salle)
        if resultat:
            self.lister_salles()



    def modifier_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        salle = Salle(code, description, categorie, capacite)
        resultat = self.service_salle.modifier_salle(salle)

        if resultat:
            self.lister_salles()



    def supprimer_salle(self):
        code = self.entry_code.get()

        resultat = self.service_salle.supprimer_salle(code)
        if resultat:
            self.lister_salles()


    def rechercher_salle(self):
        code = self.entry_code.get()

        salle = self.service_salle.rechercher_salle(code)
        if not salle :
            print("Aucune salle trouvée avec ce code.")
            return

        self.entry_description.delete(0, "end")
        self.entry_description.insert(0, salle.description)

        self.entry_categorie.delete(0, "end")
        self.entry_categorie.insert(0, salle.categorie)

        self.entry_capacite.delete(0, "end")
        self.entry_capacite.insert(0, salle.capacite)

        print("Salle trouvée et affichée")

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))
