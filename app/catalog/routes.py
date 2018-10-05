from app.catalog import main

@main.route('/')
def hello():
    return 'hello world'