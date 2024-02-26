from flask import blueprints, abort, request, jsonify, render_template
from sqlalchemy.exc import SQLAlchemyError
from src.db_instance import db
from src.models.user_model import UserModel
from wtforms import Form, StringField, PasswordField, validators

from src.views.user_view import UserView


class UserForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Length(min=8, max=80)])


user_controller = blueprints.Blueprint('user_controller', __name__)


@user_controller.route('/create_user', methods=['POST'])
def create_user():
    form = UserForm(request.form)
    if form.validate():
        try:
            user = UserModel(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return jsonify(user.as_dict())
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description="Database error")
    else:
        abort(400, description="Invalid form data")


@user_controller.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    response = UserView.get_user_view(username)
    if response.status_code == 200:
        user = response.json()
        return render_template('index.html', user=user)
    else:
        return render_template('error.html', error=response.text)


@user_controller.route('/update_user/<username>', methods=['PUT'])
def update_user(username):
    form = UserForm(request.form)
    if form.validate():
        try:
            user = UserModel.query.filter_by(username=username).first()
            if user:
                user.password = form.password.data
                db.session.commit()
                return jsonify(user.as_dict())
            else:
                abort(404, description="User not found")
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description="Database error")
    else:
        abort(400, description="Invalid form data")


@user_controller.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    try:
        user = UserModel.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            abort(404, description="User not found")
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, description="Database error")
