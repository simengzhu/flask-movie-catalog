import os

DEBUG = False
SECRET_KEY = 'DRxVxjUwSq_bigsql'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:DRxVxjUwSq_bigsql@localhost/catalog_db'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False