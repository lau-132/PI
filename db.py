from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#def run():
engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=engine)

global session
session = Session()

Base = declarative_base()

Base.metadata.create_all(engine)
