from app import create_app, db
from app.auth.models import User

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name='tyler').first():
        User.create_user(user='tyler',
                         email='tyler@durden.com',
                         password='soaps')
        flask_app.run()