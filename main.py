from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from src.item.url import URLItem

app = Flask(__name__, static_url_path='')
CORS(app)

websites = [
    URLItem('https://www.google.com'),
    URLItem('https://www.youtube.com/watch?v=btN_ge9S9No'),
]

@app.route('/websites', methods=['GET'])
def get_websites():
    return jsonify(websites)

@app.route('/websites', methods=['POST'])
def rate_website():
    data = request.get_json()
    # You could save the user's rating here, for example:
    print(f'User rated website {data["website"]} as {data["rating"]}')
    return '', 204

@app.route('/')
def index():
    print(websites[0])
    return render_template('index.html', previews=websites, base_url='https://codehost.doze.dev')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
