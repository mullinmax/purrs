import threading
import time

from flask import Flask, render_template
from flask_cors import CORS
from flask_login import LoginManager


from src.config import Config
from src.task.read_feeds import read_feeds
from src.database.session import init_db, get_db_session
from src.database.user import User

from src.routes.auth import auth_blueprint
from src.routes.feed import feed_blueprint
from src.routes.page import page_blueprint
from src.routes.theme import theme_blueprint

#
# init app and db
#
app = Flask(__name__, static_url_path='')
app.config.from_object(Config)
CORS(app)

init_db()

#
# backgorund tasks
#
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
            task()
        time.sleep(60) # run once per minute

thread = threading.Thread(target=background_job)
thread.start()

#
# init auth
#
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    with get_db_session() as session:
        return session.query(User).filter_by(id=id).first()


#
# register blueprints
#
app.register_blueprint(auth_blueprint)
app.register_blueprint(feed_blueprint)
app.register_blueprint(page_blueprint)
app.register_blueprint(theme_blueprint)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
