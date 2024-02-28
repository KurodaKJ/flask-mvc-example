from flask_sqlalchemy import SQLAlchemy

# Create a new instance of the SQLAlchemy class
db = SQLAlchemy()

# Why do we need to create a new instance of the SQLAlchemy class in db_instance.py?
# We need to create a new instance of the SQLAlchemy class in db_instance.py because we need to create a new instance
# of the SQLAlchemy class in order to use it to connect to the database without getting an error like circular import.
