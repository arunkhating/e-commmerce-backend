from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://admin:admin123@localhost:5433/ecommerce"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

from app.models import *
SessionLocal = sessionmaker(bind=engine)