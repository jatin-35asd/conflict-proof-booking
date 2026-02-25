from extensions import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    user_id = db.Column(db.Integer, nullable=False)

    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="ACTIVE"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    __table_args__ = (
        db.Index(
            "idx_room_time",
            "room_id",
            "start_time",
            "end_time"
        ),
    )