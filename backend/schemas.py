from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class HCPBase(BaseModel):
    name: str
    specialty: str
    location: str
    tier: Optional[str] = "Standard"

class HCPCreate(HCPBase):
    pass

class HCP(HCPBase):
    id: int
    
    class Config:
        orm_mode = True

class InteractionBase(BaseModel):
    hcp_id: int
    date: date
    notes: str
    products_discussed: str

class InteractionCreate(InteractionBase):
    pass

class Interaction(InteractionBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default_thread"
