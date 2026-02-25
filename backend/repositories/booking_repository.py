from models.booking import Booking
from extensions import db

class BookingRepository:

    @staticmethod
    def find_overlapping(room_id, start_time, end_time):
        return Booking.query.filter(
            Booking.room_id == room_id,
            Booking.status == "ACTIVE",
            Booking.start_time < end_time,
            Booking.end_time > start_time
        ).first()

    @staticmethod
    def save(booking):
        db.session.add(booking)
        db.session.commit()
        return booking

    @staticmethod
    def get_by_room(room_id):
        return Booking.query.filter_by(room_id=room_id).all()

    @staticmethod
    def get_by_id(booking_id):
        return Booking.query.get(booking_id)