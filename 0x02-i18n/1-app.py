#!/usr/bin/env python3
"""
Then instantiate the Babel object in your app.
Store it in a module-level variable named babel
"""
from flask import Flask, render_template
from typing import Any
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class that has a LANGUAGES class attribute
    equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    return index.html template that simply outputs
    “Welcome to Holberton” as page title (<title>) and
    “Hello world” as header (<h1>)
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
