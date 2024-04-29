"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, StringField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name:', validators=[InputRequired(), Length(min=1, max=50)])
    description = TextAreaField('Description:', validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(), Length(min=1, max=50)])
    artist = StringField('Artist', validators=[InputRequired(), Length(min=1, max=50)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
