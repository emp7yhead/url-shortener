"""App initialization."""
from app.config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)
migrate = Migrate(app, db)

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])
