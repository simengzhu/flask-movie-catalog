from app.catalog import main
from app import db
from app.catalog.models import Movie, Studio
from flask import render_template

@main.route('/')
def display_movies():

    movies = Movie.query.all()
    return render_template('home.html', movies=movies)


@main.route('/display/studio/<studio_id>')
def display_studio(studio_id):

    studio = Studio.query.filter_by(id=studio_id).first()
    studio_movies = Movie.query.filter_by(studio_id=studio.id).all()

    return render_template('studio.html', studio=studio, studio_movies=studio_movies)