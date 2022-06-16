import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Float

class Playlist(db.Base):
    __tablename__ = 'Playlists'

    playlist_id = Column(Integer, primary_key=True)
    playlist_name = Column(String)
    songs = relationship('Songs', secondary='playlist_songs')

class Songs(db.Base):
    __tablename__ = 'Songs'

    song_id = Column(Integer, primary_key=True)
    song_name = Column(String)
    song_route = Column(String)
    song_begin = Column(Float)
    song_finish = Column(Float)

    employees = relationship('Songs', secondary='playlist_songs')

