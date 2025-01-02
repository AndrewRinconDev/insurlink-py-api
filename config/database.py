import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

database = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    database=os.environ['DB_NAME']
)
