from data.dao_salle import  DataSalle
from services.service_salle import ServiceSalle
from views.view_salle import ViewSalle

data_salle = DataSalle()
service_salle = ServiceSalle(data_salle)

app = ViewSalle(service_salle)
app.mainloop()
