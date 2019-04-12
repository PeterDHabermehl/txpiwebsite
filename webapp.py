# -*- coding: utf-8 -*-
#
# TX-Pi website.
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software.
#
# If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
#
"""\
TX-Pi website.
"""
import os
import uuid
from flask import Flask, render_template
from flask_misaka import Misaka
import jinja2

app = Flask(__name__)
Misaka(app)

# Strictly, the secret key isn't needed for our purposes (mainly used for session management)
# Generate a random key anyway.
app.config['SECRET_KEY'] = str(uuid.uuid4()).encode('utf-8')

# Let template rendering fail if Jinja encounters undefined variables
app.jinja_env.undefined = jinja2.StrictUndefined


# Available TX-Pi images
import configparser
import json
_TXPI_IMAGES = configparser.ConfigParser()
_TXPI_IMAGES.read(os.path.join(os.path.dirname(__file__), 'images.ini'))
# Convert to dict for an easier access
_TXPI_IMAGES = json.loads(json.dumps(_TXPI_IMAGES._sections))
del configparser
del json


@app.route('/en/')
def home_en():
    """\
    English homepage.
    """
    return render_template('home_en.html', page_title='TX-Pi')


@app.route('/en/images/')
def images_en():
    """\
    Renders a page about the images.
    """
    images = _TXPI_IMAGES
    return render_template('images_en.html', page_title='TX-Pi Images',
                           images=images)


@app.route('/en/installation/')
def installation_en():
    """\
    Installation hints.
    """
    return render_template('installation_en.html', page_title='TX-Pi Installation')
