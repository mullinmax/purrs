import threading
import time

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.database.base import Base
from src.database.item import ItemModel

from src.task.read_feeds import read_feeds
from src.item.generic import GenericItem

app = Flask(__name__, static_url_path='')
CORS(app)

DATABASE = 'purrs.sqlite'


engine = create_engine('sqlite:///purrs.sqlite')
Session = sessionmaker(bind=engine)

# Create tables.
Base.metadata.create_all(engine)

background_tasks = [
    read_feeds
    # get_text_representations
    # get_embeddings
    # train_ml_model
    # score_items
]


def background_job():
    while True:
        for task in background_tasks:
            with Session() as session:
                task(session)
        time.sleep(3600) # wait one hour

thread = threading.Thread(target=background_job)
thread.start()

@app.route('/')
def index():
    with Session() as session:
        # query database for items
        items = session.query(ItemModel).all()
    return render_template('index.html', previews=items, base_url='https://codehost.doze.dev')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
