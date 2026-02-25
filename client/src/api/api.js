import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const getRooms = () => API.get("/rooms");
export const createRoom = (data) => API.post("/rooms", data);

export const createBooking = (data) => API.post("/bookings", data);
export const getBookings = (roomId) =>
  API.get(`/bookings?room_id=${roomId}`);
export const cancelBooking = (id) =>
  API.delete(`/bookings/${id}`);