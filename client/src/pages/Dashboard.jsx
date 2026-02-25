import React, { useState } from "react";
import RoomList from "../components/RoomList";
import BookingForm from "../components/BookingForm";
import BookingList from "../components/BookingList";
import CreateRoom from "../components/CreateRoom";

const Dashboard = () => {
  const [selectedRoom, setSelectedRoom] = useState(null);
  const [refreshKey, setRefreshKey] = useState(0);

  const triggerRefresh = () => {
    setRefreshKey(prev => prev + 1);
  };

  return (
    <div className="container">
      <CreateRoom />
      <RoomList onSelectRoom={setSelectedRoom} />
      <BookingForm
        selectedRoom={selectedRoom}
        onBookingCreated={triggerRefresh}
      />
      <BookingList
        selectedRoom={selectedRoom}
        refreshKey={refreshKey}
      />
    </div>
  );
};

export default Dashboard;