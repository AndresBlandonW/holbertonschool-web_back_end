#!/usr/bin/env python3
"""Basic Flask app"""
from urllib import response
from flask import Flask, abort, jsonify, request
import flask
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
        res = flask.make_response()
        res.set_cookie('session_id', session_id)
        return jsonify({"email": email, "message": "logged in"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
