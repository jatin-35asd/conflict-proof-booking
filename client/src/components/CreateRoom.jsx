import React, { useState } from "react";
import { createRoom } from "../api/api";

const CreateRoom = ({ refreshRooms }) => {
  const [form, setForm] = useState({
    name: "",
    capacity: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createRoom(form);
      alert("Room created");
      setForm({ name: "", capacity: "" });
      refreshRooms();
    } catch (err) {
      alert("Error creating room");
    }
  };

  return (
    <div className="card">
      <h3>Create Room</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Room Name"
          value={form.name}
          required
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />
        <input
          type="number"
          placeholder="Capacity"
          value={form.capacity}
          required
          onChange={(e) =>
            setForm({ ...form, capacity: e.target.value })
          }
        />
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default CreateRoom;