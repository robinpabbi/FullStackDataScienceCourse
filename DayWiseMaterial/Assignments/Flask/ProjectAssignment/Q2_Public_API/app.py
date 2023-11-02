from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


def get_publicAPIs_data():
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    data = get_publicAPIs_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)