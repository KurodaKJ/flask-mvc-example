from flask import blueprints, abort, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from src.db_instance import db
from src.models.user_model import UserModel

# Create a new blueprint for the user controller
user_controller = blueprints.Blueprint('user_controller', __name__)


@user_controller.route('/create_user', methods=['POST'])
def create_user():
    # Get the username and password from the request form
    username = request.form['username']
    password = request.form['password']

    try:
        # Check if user already exists
        usercheck = UserModel.query.filter_by(username=username).first()
        if usercheck:
            return jsonify({'message': 'User already exists'})

        # Store the user in the database
        user = UserModel(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        # Return a success message
        return jsonify({'message': 'User created successfully'})

    # Catch any database errors
    except SQLAlchemyError as e:

        # Rollback the database session
        db.session.rollback()

        # Return an error message
        return jsonify({'message': 'Database error' + str(e)})


@user_controller.route('/get_user', methods=['POST'])
def get_user():
    # Get the username from the request form
    username = request.form['username']

    try:
        # Get the user from the database
        user = UserModel.query.filter_by(username=username).first()

        # Return the user as a dictionary if found or not in json format
        if user:
            return jsonify({'message': 'User found'})
        else:
            return jsonify({'message': 'User not found'})

    # Catch any database errors
    except SQLAlchemyError as e:
        # Rollback the database session
        db.session.rollback()

        # Return an error message
        return jsonify({'message': 'Database error' + str(e)})


@user_controller.route('/update_user', methods=['POST'])
def update_user():
    # Get the username and password from the request form
    username = request.form['username']
    password = request.form['password']

    try:
        # Check if user exists
        user = UserModel.query.filter_by(username=username).first()
        if user:
            user.password = password
            db.session.commit() # Commit the changes to the database

            return jsonify({'message': 'User updated successfully'})
        else:
            return jsonify({'message': 'User not found'})
    except SQLAlchemyError as e:
        # Rollback the database session
        db.session.rollback()

        # Return an error message
        return jsonify({'message': 'Database error' + str(e)})


@user_controller.route('/delete_user', methods=['POST'])
def delete_user():
    # Get the username from the request form
    username = request.form['username']
    try:
        # Check if user exists
        user = UserModel.query.filter_by(username=username).first()
        if user:
            # Delete the user from the database
            db.session.delete(user)
            db.session.commit()

            # Return a success message
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User not found'})
    except SQLAlchemyError as e:
        # Rollback the database session
        db.session.rollback()

        # Return an error message
        return jsonify({'message': 'Database error' + str(e)})
