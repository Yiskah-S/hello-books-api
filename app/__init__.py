from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    # app.congif["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.congif["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5482/hello_books_development"

    # db.init_app(app)
    # migrate.init_app(app, db)

    from .routes import hello_world_bp, books_bp
    app.register_blueprint(hello_world_bp)
    app.register_blueprint(books_bp)

    return app