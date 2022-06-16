from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///productos.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

with resources.path("project.data", "author_book_publisher.db") as sqlite_filepath:
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()