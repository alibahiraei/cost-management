from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import create_engine

engine=create_engine('sqlite:///ESPENSE.db')
SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


