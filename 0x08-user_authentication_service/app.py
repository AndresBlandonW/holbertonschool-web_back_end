#!/usr/bin/env python3
"""Basic Flask app"""
from urllib import response
from flask import Flask, abort, jsonify, redirect, request, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """return register user"""
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """return sessions route"""
    email = request.form['email']
    password = request.form['password']

    req = AUTH.valid_login(email, password)

    if req is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        resp = jsonify({"email": email, "message": "logged in"})
        resp.set_cookie('session_id', session_id)
        return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout and destroy session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('home'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is not None:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """reset password token"""
    email = request.form['email']
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """update the password of user"""
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
