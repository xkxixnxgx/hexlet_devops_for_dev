import os
from datetime import timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.join(os.path.dirname(basedir), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# настройки db
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv("SECRET_KEY")
WTF_CSRF_TIME_LIMIT = None

REMEMBER_COOKIE_DURATION = timedelta(days=7)
