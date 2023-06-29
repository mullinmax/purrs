from datetime import datetime
from flask import Blueprint, request, jsonify, render_template

theme_blueprint = Blueprint('theme', __name__)

@theme_blueprint.route('/css')
def get_theme_css():
    return render_template('css/base.css'), 200, {'Content-Type': 'text/css'}
