from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")



def get_db_connection():
    """ Create and return database engine. """
    try:
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        print("✅ Database connection established successfully.")
        return engine
    except Exception as e:
        print(f"❌ Error establishing database connection: {e}")
        raise

# Test the connection
engine = get_db_connection()