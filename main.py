from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from src.task.read_feeds import read_feeds

from src.item.url import URLItem

app = Flask(__name__, static_url_path='')
CORS(app)

DATABASE = 'purrs.sqlite'

def db_task_wrapper(func):
    def f():
        with sqlite3.connect('purrs.sqlite') as db:
            func(db)
    return f

background_tasks = [
    read_feeds
    # get_text_representations
    # get_embeddings
    # train_ml_model
    # score_items
]

scheduler = BackgroundScheduler()
for task in background_tasks:
    scheduler.add_job(
        db_task_wrapper(task), # passes a database connection to each task
        'interval', 
        hours=1
    )
scheduler.start()

websites = [
    URLItem('https://www.google.com'),
    URLItem('https://www.youtube.com/watch?v=btN_ge9S9No'),
    URLItem("https://www.youtube.com/watch?v=Kd9W-t0sy4s"),
    URLItem("https://www.reddit.com/r/pics/comments/14gkznm/hide_your_mothers_john_oliver_is_back_in_town/")
]

@app.route('/')
def index():
    # query database for items with highest score
    return render_template('index.html', previews=websites, base_url='https://codehost.doze.dev')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
