from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Patient
import os

# Load DB URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/hospital_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if not already created
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hospital API is live"}

@app.post("/patients")
def create_patient(name: str, dob: str, contact: str):
    session = SessionLocal()
    patient = Patient(name=name, dob=dob, contact=contact)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    session.close()
    return {"id": patient.id, "name": patient.name}
