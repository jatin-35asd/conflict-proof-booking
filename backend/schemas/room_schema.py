from extensions import ma
from models.room import Room

class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room
        load_instance = True

room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)