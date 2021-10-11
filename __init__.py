"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import build_a_bear.views
import build_a_bear.options

