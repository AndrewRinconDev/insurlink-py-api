from services.email import sendEmail
from repositories.notification import saveEmailNotification

def sendEmailNotification(values):
  saveEmailNotification(values)
  sendEmail({
    "to": values["contactEmail"],
    "title": "Solicitud de información de productos",
    "summary": "El cliente solicita información sobre los productos a través de la página web, los datos del cliente son los siguientes:",
    "data": values
  })
  