from flask import Flask
from flask_migrate import Migrate
from src.controllers.user_controller import user_controller
from src.db_instance import db


# Create the Flask application
def create_app():
    flask_app = Flask(__name__) # Instantiate the Flask application
    flask_app.register_blueprint(user_controller) # Register the user_controller blueprint
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/example' # Set the database URI
    flask_app.config['server_name'] = 'localhost:5000' # Set the server name

    db.init_app(flask_app) # Initialize the database
    migrate = Migrate(flask_app, db) # Initialize the migration engine

    from src.models.user_model import UserModel # Import the UserModel class for the migration engine

    return flask_app # Return the Flask application


app = create_app()
