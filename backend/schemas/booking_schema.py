from extensions import ma
from models.booking import Booking
from marshmallow import validates_schema, ValidationError
from datetime import datetime

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True
        include_fk = True

    @validates_schema
    def validate_time(self, data, **kwargs):
        if data["start_time"] >= data["end_time"]:
            raise ValidationError("Start time must be before end time.")

        if data["start_time"] <= datetime.utcnow():
            raise ValidationError("Cannot book in the past.")

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)