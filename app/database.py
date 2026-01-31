from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import (
    MONGO_URI,
    MONGO_DB,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DB
)

# ---------- MongoDB ----------
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB]
mongo_collection = mongo_db["raw_characters"]

# ---------- MySQL ----------
mysql_url = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
engine = create_engine(mysql_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
