import pathlib, jinja2
import os
# from email.mime.text import MIMEText
from dotenv import load_dotenv
from mailjet_rest import Client
import os


load_dotenv()

def sendEmail(emailData):
  template = jinja2.Template(pathlib.Path("templates/email_template.html").read_text(encoding="utf-8"))

  try:
    # assigning NewEmail() without params defaults to MAILERSEND_API_KEY env var
    api_key = os.environ['MJ_APIKEY_PUBLIC']
    api_secret = os.environ['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret), version='v3')
    
    emails = emailData["to"].split(';')
    recipients = [{"Email": email, "Name": "Worker"} for email in emails]

    
    data = {
      'FromEmail': os.environ['EMAIL_USER'],
      'Recipients': recipients,
      'Subject': "Website - Solicitud de información de productos",
      'Html-part': template.render(**emailData)
    }
    
    result = mailjet.send.create(data=data)
    
    print(result.json())
    print("Email sent")
  except Exception as e:
    print("Error sending email: ", e)
    raise e