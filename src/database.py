from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from settings import DATABASE_FILE

sqlite = create_engine("sqlite:///" + DATABASE_FILE, echo=True)
base = declarative_base()

session_maker = sessionmaker(bind=sqlite)
session = session_maker()
