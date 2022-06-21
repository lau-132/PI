import db 
from models import *

def run():
    db.Base.metadata.create_all(db.engine)