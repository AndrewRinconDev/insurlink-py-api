from services.email import sendEmail

def sendEmailNotification(values):
  # TODO Save email notification

  sendEmail({
    "to": "andrew.rincon.94@gmail.com",
    "subject": "Test 2",
    "title": "Test",
    "summary": "Test",
    "url_image": "https://www.google.com"
    # "html": getEmailTemplate({ "title": "Test", "summary": "Test", "url_image": "https://www.google.com" })
  })
  