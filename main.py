import threading
import time
import sqlite3

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from src.task.read_feeds import read_feeds
from src.item.generic import GenericItem

app = Flask(__name__, static_url_path='')
CORS(app)

DATABASE = 'purrs.sqlite'

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
            with sqlite3.connect(DATABASE) as db:
                task(db)
        time.sleep(3600) # wait one hour

thread = threading.Thread(target=background_job)
thread.start()

websites = [
    GenericItem('https://www.google.com'),
    GenericItem('https://www.youtube.com/watch?v=btN_ge9S9No'),
    GenericItem("https://www.youtube.com/watch?v=Kd9W-t0sy4s"),
    GenericItem("https://www.reddit.com/r/pics/comments/14gkznm/hide_your_mothers_john_oliver_is_back_in_town/")
]

@app.route('/')
def index():
    # query database for items with highest score
    return render_template('index.html', previews=websites, base_url='https://codehost.doze.dev')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
