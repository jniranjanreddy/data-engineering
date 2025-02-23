import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv



# Enable logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Load environment variables from .env file
load_dotenv()



# MySQL
mysql_USERNAME = os.getenv("MYSQL_USERNAME")
mysql_PASSWORD = os.getenv("MYSQL_PASSWORD")
mysql_HOST = os.getenv("MYSQL_HOST")
mysql_PORT = os.getenv("MYSQL_PORT")    



## PostgreSQL
PostgreSQL_USERNAME = os.getenv("PostgreSQL_USERNAME")
PostgreSQL_PASSWORD = os.getenv("PostgreSQL_PASSWORD")
PostgreSQL_HOST = os.getenv("PostgreSQL_HOST")
PostgreSQL_PORT = os.getenv("PostgreSQL_PORT")

def test_connection(engine, db_type):
    try:
        with engine.connect() as connection:
            logger.info(f"✅ Successfully connected to {db_type} database!")
    except SQLAlchemyError as e:
        logger.error(f"❌ Failed to connect to {db_type} database: {e}")


# MySQL Connection
mysql_engine = create_engine(f"mysql+pymysql://{mysql_USERNAME}:{mysql_PASSWORD}@{mysql_HOST}:{mysql_PORT}/mydb")
test_connection(mysql_engine, "MySQL")


# PostgreSQL Connection
postgres_engine = create_engine(f"postgresql+psycopg2://{PostgreSQL_USERNAME}:{PostgreSQL_PASSWORD}@{PostgreSQL_HOST}:{PostgreSQL_PORT}/mydb")
test_connection(postgres_engine, "PostgreSQL")