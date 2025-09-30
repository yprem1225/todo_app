from flask import Flask
from app.routes.auth import auth_bp
from app.routes.tasks import tasks_bp

def create_app():
    app=Flask(__name__)
    app.secret_key="meykey"

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app



