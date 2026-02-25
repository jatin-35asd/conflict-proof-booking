import React, { useState } from "react";
import { createBooking } from "../api/api";

const BookingForm = ({ selectedRoom, onBookingCreated }) => {
  const [form, setForm] = useState({
    user_id: "",
    start_time: "",
    end_time: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createBooking({
        ...form,
        room_id: selectedRoom.id,
      });
      alert("Booking Created Successfully");
      onBookingCreated();
    } catch (err) {
      alert(err.response?.data?.message || "Booking Failed");
    }
  };

  if (!selectedRoom) return null;

  return (
    <div className="card">
      <h3>Book {selectedRoom.name}</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="User ID"
          required
          onChange={(e) =>
            setForm({ ...form, user_id: e.target.value })
          }
        />
        <input
          type="datetime-local"
          required
          onChange={(e) =>
            setForm({ ...form, start_time: e.target.value })
          }
        />
        <input
          type="datetime-local"
          required
          onChange={(e) =>
            setForm({ ...form, end_time: e.target.value })
          }
        />
        <button type="submit">Book Room</button>
      </form>
    </div>
  );
};

export default BookingForm;