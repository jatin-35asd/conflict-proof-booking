from flask import Blueprint, request, jsonify
from models.room import Room
from extensions import db
from schemas.room_schema import room_schema, rooms_schema

room_bp = Blueprint("room_bp", __name__)

@room_bp.route("/rooms", methods=["POST"])
def create_room():
    room = room_schema.load(request.json)
    db.session.add(room)
    db.session.commit()
    return room_schema.jsonify(room), 201

@room_bp.route("/rooms", methods=["GET"])
def get_rooms():
    rooms = Room.query.all()
    return rooms_schema.jsonify(rooms)