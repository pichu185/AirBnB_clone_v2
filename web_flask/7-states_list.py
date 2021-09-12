#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
