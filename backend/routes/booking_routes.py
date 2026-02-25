from flask import Blueprint, request, jsonify
from schemas.booking_schema import booking_schema, bookings_schema
from services.booking_service import BookingService
from repositories.booking_repository import BookingRepository

booking_bp = Blueprint("booking_bp", __name__)

@booking_bp.route("/bookings", methods=["POST"])
def create_booking():
    try:
        booking = booking_schema.load(request.json)
        saved = BookingService.create_booking(booking)
        return booking_schema.jsonify(saved), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 409

@booking_bp.route("/bookings", methods=["GET"])
def get_bookings():
    room_id = request.args.get("room_id")
    if room_id is None:
        return bookings_schema.jsonify([])

    room_id = int(room_id)

    bookings = BookingRepository.get_by_room(room_id)
    return bookings_schema.jsonify(bookings)

@booking_bp.route("/bookings/<int:id>", methods=["DELETE"])
def cancel_booking(id):
    try:
        BookingService.cancel_booking(id)
        return jsonify({"message": "Cancelled"})
    except Exception as e:
        return jsonify({"message": str(e)}), 400