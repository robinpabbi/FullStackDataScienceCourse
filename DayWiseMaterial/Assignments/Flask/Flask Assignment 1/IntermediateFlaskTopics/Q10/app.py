from flask import Flask, render_template

app = Flask(__name__)

# Custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

# Custom 500 error page
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('internal_error.html'), 500

@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/demo_error')
def demo_error():
    return render_template('ewrewrewewrw.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)
