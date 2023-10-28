from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Route for homepage
@app.route('/')
def display_hello_world():
    return 'Hello World'


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)