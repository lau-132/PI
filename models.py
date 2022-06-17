import db
from sqlalchemy import Column, Integer, String, Float, Time,ForeignKey
from sqlalchemy.orm import relationship

class Playlist(db.Base):
    __tablename__ = 'playlists'
    playlist_id = Column(Integer, primary_key=True)
    playlist_name = Column(String)
    songs = relationship('Song', secondary='playlists_songs_exchanges')
    exchanges = relationship('Exchange', secondary='playlists_songs_exchanges')
    
class Song(db.Base):
    __tablename__ = 'songs'
    song_id = Column(Integer, primary_key=True)
    song_name = Column(String)
    song_route = Column(String)
    song_begin = Column(Float)
    song_finish = Column(Float)
    playlists = relationship('Playlist', secondary='playlists_songs_exchanges')
    exchanges = relationship('Exchange', secondary='playlists_songs_exchanges')
    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(song_name=name).first()

    def save(self):
        db.s.add(self)
        db.s.commit()

class Exchange (db.Base):
    __tablename__ = 'exchanges'
    exchange_name = Column(String, primary_key=True)
    day_week = Column(Integer)
    play_hour = Column(Time)

class Playlist_Song_Exchange(db.Base):
    __tablename__= 'playlists_songs_exchanges'
    p_id = Column(Integer, ForeignKey('playlists.playlist_id'), primary_key=True)
    s_id = Column(Integer, ForeignKey('songs.song_id'), primary_key=True)
    e_name = Column(String, ForeignKey('exchanges.exchange_name'), primary_key=True, nullable=True)