# backend/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://neura:aemGen123!@localhost:5432/neuragendev")
    SQLALCHEMY_TRACK_MODIFICATIONS = True