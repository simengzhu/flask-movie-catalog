from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired()])
    submit = SubmitField('Update')



class CreateMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired()])
    release_date = StringField('Release Date', validators=[DataRequired()])
    studio_id = IntegerField('Studio ID', validators=[DataRequired()])
    submit = SubmitField('Create')
