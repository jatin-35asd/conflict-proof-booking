import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://booking_user:StrongPassword123!@localhost/booking_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False