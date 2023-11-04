from flask import Flask, redirect, url_for, session, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = 'MyAppSecretSalt'  # Change this to a secure key

# Setup Google OAuth
google_bp = make_google_blueprint(client_id='736752253983-f8v9k9o6vutt4prum98m5u3o449vd4k3.apps.googleusercontent.com',
                                   client_secret='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',
                                   redirect_to='google_login',
                                   redirect_url='/google_login/google/authorized')
app.register_blueprint(google_bp, url_prefix='/google_login')

@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/plus/v1/people/me')
    assert resp.ok, resp.text
    return 'Logged in as: {}'.format(resp.json()['displayName'])


@app.route('/')
def home():
    if google.authorized:
        return redirect(url_for('google_login'))
    return render_template('index.html')

@app.route('/google_login/google/authorized')
def google_login_auth():
    return redirect(url_for('google_login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5051)
