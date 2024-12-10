from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from app.config import Config
from flask_cors import CORS

db = SQLAlchemy()
swagger = Swagger()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    swagger.init_app(app)

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    with app.app_context():
        db.create_all()

    return app