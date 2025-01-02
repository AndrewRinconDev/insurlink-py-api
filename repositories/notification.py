import config.database as db
from datetime import datetime
import mysql.connector

def saveEmailNotification(values):
  try:
    if not db.database.is_connected():
      db.database.connect()
    
    cursor = db.database.cursor()
    query = """
    INSERT INTO insurlink.notification (Name, Phone, Email, Date, Insurance, Message, ContactName, ContactEmail)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    data= (values['name'], values['phone'], values['email'], datetime.now(), values['insurance'], values['message'], values['contactName'], values['contactEmail'])
    cursor.execute(query, data)
    db.database.commit()
  except mysql.connector.Error as error:
    print(f"Failed to insert record into notification table {error}")
  finally:
    if db.database.is_connected():
      db.database.close()
      print("MySQL connection is closed")