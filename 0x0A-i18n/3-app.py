#!/usr/bin/env python3
""""Basic Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize Flask-Babel
babel = Babel(app)


class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """template index"""
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """get locate an select the best language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
