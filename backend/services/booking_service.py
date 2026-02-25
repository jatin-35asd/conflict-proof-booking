from repositories.booking_repository import BookingRepository
from extensions import db
from datetime import datetime

class BookingService:

    @staticmethod
    def create_booking(booking):
        overlapping = BookingRepository.find_overlapping(
            booking.room_id,
            booking.start_time,
            booking.end_time
        )

        if overlapping:
            raise ValueError("Room already booked for this time slot.")

        return BookingRepository.save(booking)

    @staticmethod
    def cancel_booking(booking_id):
        booking = BookingRepository.get_by_id(booking_id)

        if not booking:
            raise ValueError("Booking not found.")

        if booking.end_time < datetime.utcnow():
            raise ValueError("Cannot cancel completed booking.")

        booking.status = "CANCELLED"
        db.session.commit()