import json
import os

from flask import render_template
from werkzeug.exceptions import NotFound

from app import app


@app.route("/")
def index():

    components = os.listdir("govuk_components")
    components.sort()

    return render_template("index.html", components=components)


@app.route("/components/<string:component>")
def component(component):
    try:
        with open("govuk_components/{}/fixtures.json".format(component)) as json_file:
            fixtures = json.load(json_file)
    except FileNotFoundError:
        raise NotFound

    return render_template("component.html", fixtures=fixtures)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server(error):
    return render_template("500.html"), 500

