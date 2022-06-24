#!/usr/bin/env python3
""" Module of Index views
"""
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400

    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.email == email and not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            session_name = getenv('SESSION_NAME')
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(session_name, session_id)
            return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Handles logout of current session"""
    from api.v1.app import auth

    result = auth.destroy_session(request)
    if not result:
        abort(404)

    return jsonify({}), 200
