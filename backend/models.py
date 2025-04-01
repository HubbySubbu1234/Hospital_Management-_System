from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base  # ✅ Use this import

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"  # ✅ Correct spelling

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dob = Column(Date)
    contact = Column(String)
