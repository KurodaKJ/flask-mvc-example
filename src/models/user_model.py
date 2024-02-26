from werkzeug.security import generate_password_hash
from src.db_instance import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column('password', db.String(120), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def as_dict(self):
        return {c.name: getattr(self, '_password') if c.name == 'password' else getattr(self, c.name) for c in self.__table__.columns}
