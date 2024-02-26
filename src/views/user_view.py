import requests
from flask import url_for


class UserView:
    @staticmethod
    def create_user_view(username, password):
        response = requests.post(url_for('user_controller.create_user'),
                                 data={'username': username, 'password': password})
        return response

    @staticmethod
    def get_user_view(username):
        response = requests.get(url_for('user_controller.get_user', username=username))
        return response

    @staticmethod
    def update_user_view(username, new_password):
        response = requests.put(url_for('user_controller.update_user', username=username),
                                data={'password': new_password})
        return response

    @staticmethod
    def delete_user_view(username):
        response = requests.delete(url_for('user_controller.delete_user', username=username))
        return response
