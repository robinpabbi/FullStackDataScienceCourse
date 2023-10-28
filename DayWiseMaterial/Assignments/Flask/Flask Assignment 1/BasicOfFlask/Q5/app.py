from flask import Flask, render_template, request, session

# intialize app
app = Flask(__name__)

app.secret_key = b'_5#324sfwdsdfy2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html', name=session.get('name'))

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    session['name'] = name
    return render_template('index.html', name=name)


# Start the app
if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5051)