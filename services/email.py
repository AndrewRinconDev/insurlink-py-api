import smtplib, email, pathlib, jinja2, ssl
# import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def sendEmail(emailData):
  # Load email template
  template = jinja2.Template(pathlib.Path("templates/email_template.html").read_text(encoding="utf-8"))
  msg = MIMEText(template.render(**emailData), 'html')
  # msg = MIMEText("dskfjsd")
  msg['Subject'] = emailData["subject"]
  msg['From'] = "paginaweb@insurlink.com.co"
  msg['To'] = emailData["to"]
  
  context = ssl.create_default_context()
  
  # Send email
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login("paginaweb@insurlink.com.co", "qgpa efdv ocup vanu")
    server.sendmail("paginaweb@insurlink.com.co", emailData["to"], msg.as_string())
    server.quit()
    
  print("Email sent")