from app.catalog import main
from app import db
from app.catalog.models import Movie, Studio
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required

@main.route('/')
def display_movies():

    movies = Movie.query.all()
    return render_template('home.html', movies=movies)


@main.route('/display/studio/<studio_id>')
def display_studio(studio_id):

    studio = Studio.query.filter_by(id=studio_id).first()
    studio_movies = Movie.query.filter_by(studio_id=studio.id).all()

    return render_template('studio.html', studio=studio, studio_movies=studio_movies)


@main.route('/movie/delete/<movie_id>', methods=['GET', 'POST'])
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        flash('movie deleted successfully')
        return redirect(url_for('main.display_movies'))

    return render_template('delete_movie.html', movie=movie, movie_id=movie.id)
