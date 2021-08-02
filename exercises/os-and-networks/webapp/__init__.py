from flask import Flask, redirect, url_for
from flask_login import LoginManager
from webapp.config import SECRET_KEY, WTF_CSRF_TIME_LIMIT
from flask_wtf.csrf import CSRFProtect
from webapp.model import db
from webapp.picture.models import Picture
from webapp.comment.models import Comment
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.picture.views import blueprint as picture_blueprint
from webapp.comment.views import blueprint as comment_blueprint


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.config['SECRET_KEY'] = SECRET_KEY

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(picture_blueprint)
    app.register_blueprint(comment_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        return redirect(url_for('picture.pictures'))

    if __name__ == '__main__':
        app.run(debug=True)

    return app






