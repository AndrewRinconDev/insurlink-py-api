from flask import Flask
from flask_cors import CORS;
from controller.notification import notification_bp


def create_app():
  app = Flask(__name__)
  CORS(app)

  # Register the blueprint
  app.register_blueprint(notification_bp)

  return app


