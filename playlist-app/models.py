"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    playlist_songs = db.relationship('PlaylistSong', backref='playlist', cascade='all, delete-orphan')


class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    song = db.relationship('Song', backref='playlist_songs')

    def __repr__(self):
        return f'<PlaylistSong id={self.id} playlist_id={self.playlist_id} song_id={self.song_id}>'


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    
    db.app = app
    db.init_app(app)
