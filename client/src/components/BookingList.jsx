import React, { useEffect, useState } from "react";
import { getBookings, cancelBooking } from "../api/api";

const BookingList = ({ selectedRoom, refreshKey }) => {
  const [bookings, setBookings] = useState([]);

  const fetchBookings = () => {
    if (selectedRoom) {
      getBookings(selectedRoom.id).then((res) =>
        setBookings(res.data)
      );
    }
  };

  useEffect(() => {
  if (selectedRoom) {
    getBookings(selectedRoom.id).then((res) =>
      setBookings(res.data)
    );
  }
}, [selectedRoom, refreshKey]); 

  const handleCancel = async (id) => {
    await cancelBooking(id);
    fetchBookings();
  };

  if (!selectedRoom) return null;

  return (
    <div className="card">
      <h3>Bookings</h3>
      {bookings.map((b) => (
        <div key={b.id} className="booking-item">
          <div>
            {new Date(b.start_time).toLocaleString()} →{" "}
            {new Date(b.end_time).toLocaleString()}
          </div>
          <button onClick={() => handleCancel(b.id)}>
            Cancel
          </button>
        </div>
      ))}
    </div>
  );
};

export default BookingList;