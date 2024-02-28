from flask import Flask
from flask_migrate import Migrate

from src.controllers.user_controller import user_controller
from src.db_instance import db


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(user_controller)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/example'
    flask_app.config['server_name'] = 'localhost:5000'

    db.init_app(flask_app)
    migrate = Migrate(flask_app, db)

    from src.models.user_model import UserModel

    return flask_app


app = create_app()
