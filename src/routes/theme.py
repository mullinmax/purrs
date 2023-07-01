from datetime import datetime
from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required


theme_blueprint = Blueprint('theme', __name__)

@theme_blueprint.route('/css')
@login_required
def get_theme_css():
    return render_template('css/base.css'), 200, {'Content-Type': 'text/css'}
