from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///property_rental_management.db"
engine = create_engine(DB_URL)
Base = declarative_base()


Base.metadata.create_all(engine)