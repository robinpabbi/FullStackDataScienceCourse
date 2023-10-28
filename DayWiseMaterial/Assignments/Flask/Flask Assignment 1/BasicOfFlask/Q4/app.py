from flask import Flask, render_template, request

# intialize app
flask_app = Flask(__name__)

@flask_app.route('/')
def home_page():
    return render_template('index.html')


@flask_app.route('/submit', methods=['POST'])
def submit_username():
    name = request.form.get('name')
    return f'Hello! {name}'


# Start the app
if(__name__ == '__main__'):
    flask_app.run(host='0.0.0.0', port=5051)