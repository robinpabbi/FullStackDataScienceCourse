from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User

app = Flask(__name__)
app.secret_key = 'MyAppSecretSalt'  # Change this to your actual secret key

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    # Retrieve user from your database by user_id
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']  # Get user id from form
        # Validate user credentials (e.g., check against database)
        if user_is_valid(user_id):
            user = User(user_id)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


def user_is_valid(user_id):
    # Hardcoded list of valid users
    valid_users = [
        {'user_id': 'robin', 'password': 'password123'},
        {'user_id': 'robinpabbi', 'password': 'pabbi'}
    ]

    # Check if the provided user_id exists in the list of valid users
    user = next((user for user in valid_users if user['user_id'] == user_id), None)

    if user is not None:
        return user
    else:
        return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)