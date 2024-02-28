from werkzeug.security import generate_password_hash
from src.db_instance import db


# Example of a user model for the database
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column('password', db.String(120), nullable=False)

    # This is a getter method for the password property
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    # This is a setter method for the password property
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password) # Hash the password

    # This method returns a dictionary representation of the user model
    def as_dict(self):
        return {c.name: getattr(self, '_password') if c.name == 'password' else getattr(self, c.name) for c in self.__table__.columns}
