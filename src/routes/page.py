from datetime import datetime
from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required

from src.database.feed import FeedModel
from src.database.item import ItemModel
from src.database.session import get_db_session

page_blueprint = Blueprint('page', __name__)

@page_blueprint.route('/config/feeds', methods=['GET'])
@login_required
def manage_feeds():
    with get_db_session() as session:
        feeds = session.query(FeedModel).all()
    return render_template('html/feeds.jinja', feeds=feeds)

@page_blueprint.route('/')
@login_required
def index():
    with get_db_session() as session:
        items = session.query(ItemModel).all()
    return render_template('html/index.jinja', previews=items)
