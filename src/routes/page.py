from flask import Blueprint, request, jsonify
from src.database.feed import FeedModel
from datetime import datetime
from src.database.session import db_session

page_blueprint = Blueprint('feed', __name__)

@page_blueprint.route('/feeds/manage', methods=['GET'])
def manage_feeds():
    feeds = db_session.query(FeedModel).all()
    return render_template('feeds.html', feeds=feeds)

@page_blueprint.route('/')
def index():
    items = db_session.query(ItemModel).all()
    return render_template('index.jinja', previews=items, base_url='https://codehost.doze.dev')