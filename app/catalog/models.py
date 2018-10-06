from app import db
from datetime import datetime



class Studio(db.Model):
    __tablename__ = 'studio'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Studio is {}'.format(self.name)


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable=False, index=True)
    director = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    genre = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    length = db.Column(db.Integer)
    release_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship
    studio_id = db.Column(db.Integer, db.ForeignKey('studio.id'))

    def __init__(self, title, director, avg_rating, movie_genre, image, movie_length, date, studio_id):

        self.title = title
        self.director = director
        self.avg_rating = avg_rating
        self.genre = movie_genre
        self.image = image
        self.length = movie_length
        self.release_date = datetime.strptime(date, '%m/%d/%Y')
        self.studio_id = studio_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.director)


