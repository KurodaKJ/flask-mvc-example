from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from src.db_instance import db
from src.models.user_model import UserModel


def create_user(username, password):
    try:
        user = UserModel(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        return user
    except SQLAlchemyError as e:
        db.session.rollback()
        return str(e)
