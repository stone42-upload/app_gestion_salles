import customtkinter as ctk

class ViewSalle(ctk.CTk):
    def __init__(self, service_salle):
        super().__init__()

        self.service_salle = service_salle

        self.title("Gestion des Salles")
        self.geometry("600x400")

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=20 ,padx="top", fill="x")

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
