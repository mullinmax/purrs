from flask import Blueprint, request, jsonify
from src.database.feed import FeedModel
from datetime import datetime
from src.database.session import get_db_session

feed_blueprint = Blueprint('feed', __name__)

@feed_blueprint.route('/feeds', methods=['GET'])
def get_feeds():
    with get_db_session() as session:
        feeds = session.query(FeedModel).all()
    return jsonify([feed.__dict__ for feed in feeds]), 200

@feed_blueprint.route('/feeds', methods=['POST'])
def create_feed():
    with get_db_session() as session:
        data = request.get_json()
        new_feed = FeedModel(
            url=data['url'],
            last_pulled=datetime.now()
        )
        session.add(new_feed)
        session.commit()
    return jsonify(new_feed.__dict__), 201

@feed_blueprint.route('/feeds/<int:id>', methods=['PUT'])
def update_feed(id):
    with get_db_session() as session:
        data = request.get_json()
        feed = session.query(FeedModel).filter(FeedModel.id == id).first()
        if feed:
            feed.url = data.get('url', feed.url)
            session.commit()
            return jsonify(feed.__dict__), 200
        else:
            return jsonify({'error': 'Feed not found'}), 404

@feed_blueprint.route('/feeds/<int:id>', methods=['DELETE'])
def delete_feed(id):
    with get_db_session() as session:
        feed = session.query(FeedModel).filter(FeedModel.id == id).first()
        if feed:
            session.delete(feed)
            session.commit()
            return jsonify({'message': 'Feed deleted'}), 200
        else:
            return jsonify({'error': 'Feed not found'}), 404
