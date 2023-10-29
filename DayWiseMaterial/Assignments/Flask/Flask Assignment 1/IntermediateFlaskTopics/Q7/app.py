from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)
app.config["DATABASE"] = 'items.db'
app.secret_key = 'appSuperSecretSalt'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db


@app.route('/')
def index():
    cursor = get_db().execute('SELECT * FROM items')
    items = cursor.fetchall()
    cursor.close()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.form['name']
    cursor = get_db().execute('INSERT INTO items (name) VALUES (?)', (name,))
    get_db().commit()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
        cursor = get_db().execute('SELECT * FROM items WHERE id = ?', (item_id,))
        item = cursor.fetchone()
        cursor.close()
        return render_template('edit_item.html', item=item)

@app.route('/edit_item/<int:item_id>', methods=['POST'])
def edit_item(item_id):
    new_name = request.form['new_name']
    cursor = get_db().execute('UPDATE items SET name = ? WHERE id = ?', (new_name, item_id))
    get_db().commit()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    cursor = get_db().execute('DELETE FROM items WHERE id = ?', (item_id,))
    get_db().commit()
    cursor.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)