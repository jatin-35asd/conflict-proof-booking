import React, { useEffect, useState } from "react";
import { getRooms } from "../api/api";

const RoomList = ({ onSelectRoom }) => {
  const [rooms, setRooms] = useState([]);

  const fetchRooms = async () => {
    const res = await getRooms();
    setRooms(res.data);
  };

  useEffect(() => {
    fetchRooms();
  }, []);

  return (
    <div className="card">
      <h3>Available Rooms</h3>

      {rooms.length === 0 && <p>No rooms yet</p>}

      {rooms.map((room) => (
        <div
          key={room.id}
          className="room-item"
          onClick={() => onSelectRoom(room)}
        >
          {room.name} (Capacity: {room.capacity})
        </div>
      ))}
    </div>
  );
};

export default RoomList;