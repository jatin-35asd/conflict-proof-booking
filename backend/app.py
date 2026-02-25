from flask import Flask
from config import Config
from flask_cors import CORS
from extensions import db, ma
from logging_config import setup_logging
from routes.room_routes import room_bp
from routes.booking_routes import booking_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    CORS(app)

    setup_logging()

    app.register_blueprint(room_bp)
    app.register_blueprint(booking_bp)

    with app.app_context():
        from models.user import User
        from models.booking import Booking
        from models.room import Room
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000)