from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String)
    location = Column(String)
    tier = Column(String, default="Standard")

    interactions = relationship("Interaction", back_populates="hcp")
    follow_ups = relationship("FollowUpAction", back_populates="hcp")

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcps.id"))
    date = Column(Date)
    notes = Column(Text)
    products_discussed = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    hcp = relationship("HCP", back_populates="interactions")

class FollowUpAction(Base):
    __tablename__ = "follow_up_actions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcps.id"))
    description = Column(String)
    due_date = Column(Date)
    status = Column(String, default="Pending")

    hcp = relationship("HCP", back_populates="follow_ups")
