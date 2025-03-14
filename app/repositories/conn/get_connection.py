import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

# Database connection parameters
DB_CONFIG = {
    'dbname': os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("DB_PORT")
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

