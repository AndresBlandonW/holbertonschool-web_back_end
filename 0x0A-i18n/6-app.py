#!/usr/bin/env python3
""""Basic Flask app"""
from flask_babel import Babel
from flask import Flask, g, render_template, request

app = Flask(__name__)

# Initialize Flask-Babel
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """template index"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """get locate an select the best language"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    accepted = request.headers.get('Accept-Language')
    if accepted and accepted in app.config['LANGUAGES']:
        return accepted

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """return user dictionary"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """Find a user if any, and set it as a global"""
    g.user = get_user()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
