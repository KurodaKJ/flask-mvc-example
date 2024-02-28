from flask import blueprints, abort, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from src.db_instance import db
from src.models.user_model import UserModel

user_controller = blueprints.Blueprint('user_controller', __name__)


@user_controller.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    try:
        # Check if user already exists
        usercheck = UserModel.query.filter_by(username=username).first()
        if usercheck:
            return jsonify({'message': 'User already exists'})
        user = UserModel(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error' + str(e)})


@user_controller.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    try:
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return jsonify(user.as_dict())
        else:
            return jsonify({'message': 'User not found'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error' + str(e)})


@user_controller.route('/update_user', methods=['POST'])
def update_user():
    username = request.form['username']
    password = request.form['password']
    try:
        user = UserModel.query.filter_by(username=username).first()
        if user:
            user.password = password
            db.session.commit()
            return jsonify({'message': 'User updated successfully'})
        else:
            return jsonify({'message': 'User not found'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error' + str(e)})


@user_controller.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    try:
        user = UserModel.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User not found'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Database error' + str(e)})
