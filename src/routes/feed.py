from flask import Blueprint, request, jsonify
from flask_login import login_required
from datetime import datetime

from src.database.feed import FeedModel
from src.database.session import get_db_session

feed_blueprint = Blueprint('feed', __name__)

@feed_blueprint.route('/feeds', methods=['GET'])
@login_required
def get_feeds():
    with get_db_session() as session:
        feeds = session.query(FeedModel).all()
    return jsonify([feed.to_dict() for feed in feeds]), 200

@feed_blueprint.route('/feeds', methods=['POST'])
@login_required
def create_feed():
    with get_db_session() as session:
        data = request.get_json()
        new_feed = FeedModel(
            url=data['url'],
            cron_expression=data['cron_expression']
        )
        session.add(new_feed)
        session.commit()
        new_feed_dict = new_feed.to_dict()
    return jsonify(new_feed_dict), 201

@feed_blueprint.route('/feeds/<int:id>', methods=['PUT'])
@login_required
def update_feed(id):
    with get_db_session() as session:
        data = request.get_json()
        feed = session.query(FeedModel).filter(FeedModel.id == id).first()
        if feed:
            feed.url = data.get('url', feed.url)
            feed.cron_expression = data.get('cron_expression', feed.cron_expression)
            session.commit()
            return jsonify(feed.to_dict()), 200
        else:
            return jsonify({'error': 'Feed not found'}), 404

@feed_blueprint.route('/feeds/<int:id>', methods=['DELETE'])
@login_required
def delete_feed(id):
    with get_db_session() as session:
        feed = session.query(FeedModel).filter(FeedModel.id == id).first()
        if feed:
            session.delete(feed)
            session.commit()
            return jsonify({'message': 'Feed deleted'}), 200
        else:
            return jsonify({'error': 'Feed not found'}), 404
