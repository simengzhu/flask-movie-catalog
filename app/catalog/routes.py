from app.catalog import main
from app import db
from app.catalog.models import Movie, Studio
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditMovieForm, CreateMovieForm

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


@main.route('/edit/movie/<movie_id>', methods=['GET', 'POST'])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get(movie_id)
    form = EditMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.title = form.title.data
        movie.format = form.format.data
        movie.num_pages = form.length.data
        db.session.add(movie)
        db.session.commit()
        flash('Book Edited Successfully')
        return redirect(url_for('main.display_movies'))
    return render_template('edit_movie.html', form=form)


@main.route('/create/movie/<studio_id>', methods=['GET', 'POST'])
@login_required
def create_movie(studio_id):
    form = CreateMovieForm()
    form.studio_id.data = studio_id

    if form.validate_on_submit():
        movie = Movie(
            title=form.title.data,
            director=form.director.data,
            avg_rating=form.avg_rating.data,
            movie_genre=form.genre.data,
            image=form.img_url.data,
            movie_length=form.length.data,
            date=form.release_date.data,
            studio_id=form.studio_id.data
        )

        db.session.add(movie)
        db.session.commit()
        flash('Movie added successfully')

        return redirect(url_for('main.display_studio', studio_id=studio_id))
    return render_template('create_movie.html', form=form, studio_id=studio_id)
