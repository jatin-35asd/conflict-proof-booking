# Conflict-Proof Room Booking System

## Overview

This project is a small, rule-driven booking system built using:

- Backend: Python + Flask
- Frontend: React (Vite)
- Database: MySQL (Relational)
- ORM: SQLAlchemy
- Validation: Marshmallow

The system guarantees that no two bookings for the same room overlap in time.

The focus of this project is correctness, structure, and change resilience — not feature count.

---

## Core Problem

Booking systems often allow accidental double-bookings due to missing validation.

This system enforces:

1. No overlapping bookings per room
2. Start time must be before end time
3. Cannot book in the past
4. Clear API validation and schema enforcement

---

## Architecture

Frontend (React)
↓
API Layer (Axios)
↓
Flask Routes (Controller Layer)
↓
Service Layer (Business Rules)
↓
Repository Layer (Data Access)
↓
MySQL (Relational DB)

### Layer Responsibilities

- Routes: Handle HTTP & response formatting only
- Services: Enforce business rules
- Repositories: Database access logic
- Schemas: Input validation & serialization
- Models: Data structure definitions

This separation ensures clarity and evolvability.

---

## Business Rule: Overlap Detection

Two bookings overlap if:

new.start < existing.end  
AND  
new.end > existing.start  

This logic ensures conflict-free reservations.

---

## Database Design

Tables:
- rooms
- bookings

Indexes:
- Composite index on (room_id, start_time, end_time)

Constraints:
- NOT NULL enforcement
- Time validation
- Status tracking

---

## API Endpoints

### Rooms
- GET /rooms
- POST /rooms

### Bookings
- POST /bookings
- GET /bookings?room_id=<id>
- DELETE /bookings/<id>

---

## AI Usage

AI tools were used to:

- Scaffold project structure
- Generate initial boilerplate code
- Suggest validation patterns

All generated code was:
- Reviewed manually
- Refactored for clarity
- Tested for correctness
- Constrained via AI guidance files

AI was not allowed to:
- Introduce hidden logic
- Modify service boundaries
- Bypass validation layers

See `/ai-guidance` folder for constraints.

---

## Setup Instructions

### 1. Clone repository

git clone <repo-url>
cd conflict-proof-booking

---

### 2. Backend Setup

cd backend

Create virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Ensure MySQL is running.

Create database:

CREATE DATABASE booking_db;

Update config.py if needed.

Run backend:

python app.py

Backend runs at:
http://localhost:8000

---

### 3. Frontend Setup

cd frontend

Install dependencies:

npm install

Run frontend:

npm run dev

Frontend runs at:
http://localhost:5173

---

## Design Decisions

- Relational DB chosen for strong consistency
- Layered architecture for change resilience
- Explicit validation to prevent invalid state
- Service layer ensures rule isolation
- Minimal feature scope to maintain clarity

---

## Known Limitations

- No authentication
- No timezone normalization
- No concurrency locking for high-scale systems

---

## Extension Ideas

- Recurring bookings
- User accounts
- Role-based access
- Optimistic locking
- Notification system
- Booking approval workflow

---

## Evaluation Focus

This system prioritizes:

- Simplicity over cleverness
- Correctness over feature count
- Structure over speed
- Explicit validation over implicit assumptions

---

End of README