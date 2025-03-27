from flask import Flask
from app.config import Config
from app.routes.auth_routes import auth_bp
from app.routes.public_routes import public_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(public_bp, url_prefix='/')

    return app
