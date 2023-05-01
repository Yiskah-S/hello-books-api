from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def create_books():
    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        )
    
    db.session.add(new_book)
    db.session.commit()

    message = f"Book {new_book.title} succesfully created"
    return make_response(message, 201)
    
@books_bp.route("", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    book_result = []
    for book in books:
        book_result.append(
            dict(
            id=book.id,
            title=book.title,
            description=book.description
            )
        )
    return jsonify(book_result), 200

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)
    
    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))
    
    return book

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = validate_book(book_id)
    book_response = {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    return jsonify(book_response), 200

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")

# from app import db
# from app.models.book import Book
# from flask import Blueprint, jsonify, make_response, request

# books_bp = Blueprint("books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["POST"])
# def handle_books():
#     request_body = request.get_json()
#     new_book = Book(title=request_body["title"],
#                     description=request_body["description"])

#     db.session.add(new_book)
#     db.session.commit()

#     return make_response(f"Book {new_book.title} successfully created", 201)




# from flask import Blueprint, jsonify, abort, make_response

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title A", "A fantasy novel set in an abc imaginary world."),
#     Book(2, "Fictional Book Title B", "A fantasy novel set in an xyz imaginary world."),
#     Book(3, "Fictional Book Title B", "A fantasy novel set in an 123 imaginary world.")
# ] 

# books_bp = Blueprint("books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response), 200

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book
#     abort(make_response({"message":f"book {book_id} not found"}, 404))

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
#     book_response = {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     }
#     return jsonify(book_response), 200







# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body, 200

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name" : "Calico",
#         "message" : "She's a little kitten.",
#         "personality" : ["Naughty", "Nice", "Curious"]
#     }, 200

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"] + new_hobby
#     return response_body
