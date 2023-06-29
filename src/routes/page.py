from datetime import datetime
from flask import Blueprint, request, jsonify, render_template

from src.database.feed import FeedModel
from src.database.item import ItemModel
from src.database.session import get_db_session

page_blueprint = Blueprint('page', __name__)

@page_blueprint.route('/config/feeds', methods=['GET'])
def manage_feeds():
    with get_db_session() as session:
        feeds = session.query(FeedModel).all()
    return render_template('html/feeds.jinja', feeds=feeds)

@page_blueprint.route('/')
def index():
    with get_db_session() as session:
        items = session.query(ItemModel).all()
    return render_template('html/index.jinja', previews=items, base_url='https://codehost.doze.dev')
