from flask import Flask, jsonify, request
from models import books, Book

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify([book.__dict__ for book in books])

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book.id == book_id), None)
    if book:
        return jsonify(book.__dict__)
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_id = max(book.id for book in books) + 1
    new_book = Book(new_id, data['title'], data['author'])
    books.append(new_book)
    return jsonify(new_book.__dict__), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book.id == book_id), None)
    if book:
        book.title = data['title']
        book.author = data['author']
        return jsonify(book.__dict__)
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book.id != book_id]
    return jsonify({'message': 'Book deleted'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)
