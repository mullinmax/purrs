import threading
import time

from flask import Flask, render_template
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.database.base import Base
from src.database.item import ItemModel
from src.task.read_feeds import read_feeds
from src.routes.feed import feed_blueprint

app = Flask(__name__, static_url_path='')
CORS(app)

DATABASE = 'purrs.sqlite'
engine = create_engine(f'sqlite:///{DATABASE}')
Session = sessionmaker(bind=engine)

# Create tables.
Base.metadata.create_all(engine)

background_tasks = [
    read_feeds,
    # Uncomment the following tasks when they're ready to be used
    # get_text_representations,
    # get_embeddings,
    # train_ml_model,
    # score_items,
]

def background_job():
    while True:
        for task in background_tasks:
            with Session() as session:
                task(session)
        time.sleep(3600)  # Wait one hour

thread = threading.Thread(target=background_job)
thread.start()

app.register_blueprint(feed_blueprint)

@app.route('/')
def index():
    with Session() as session:
        items = session.query(ItemModel).all()
    return render_template('index.jinja', previews=items, base_url='https://codehost.doze.dev')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
