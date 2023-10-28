from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Route for homepage
@app.route('/<username>')
def welcome_page(username):
    return render_template('index.html', name=username)


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)