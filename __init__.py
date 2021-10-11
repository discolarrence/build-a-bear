"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.secret_key = 'rfeuuerui48sd*fn%fvjdkna;ep2340fm'

import build_a_bear.views
import build_a_bear.options

