from flask import Flask
from flask_migrate import Migrate
from src.db_instance import db


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/example'

    db.init_app(flask_app)
    migrate = Migrate(flask_app, db)

    from src.models.user_model import UserModel

    return flask_app


app = create_app()
