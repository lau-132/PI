from datetime import datetime
import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime

class Playlist(db.Base):
    __tablename__ = 'playlists'

    playlist_id = Column(Integer, primary_key=True)
    playlist_name = Column(String)
    songs = relationship('Songs', secondary='playlists_songs')

class Songs(db.Base):
    __tablename__ = 'songs'

    song_id = Column(Integer, primary_key=True)
    song_name = Column(String)
    song_route = Column(String)
    song_begin = Column(Float)
    song_finish = Column(Float)

    playlists = relationship('Playlists', secondary='playlists_songs')

class Playlist_Songs(db.Base):
    __tablename__= 'playlists_songs'

    p_id = Column(Integer, ForeignKey('playlists.playlist_id'), primary_key=True)
    s_id = Column(Integer, ForeignKey('songs.song_id'), primary_key=True)
    play_time = Column(datetime, primary_key=True)
