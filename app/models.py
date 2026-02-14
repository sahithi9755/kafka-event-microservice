from pydantic import BaseModel, Field
from typing import Dict, Any
from uuid import uuid4
from datetime import datetime

class UserEventRequest(BaseModel):
    userId: str
    eventType: str
    payload: Dict[str, Any] = {}

class UserEvent(BaseModel):
    eventId: str = Field(default_factory=lambda: str(uuid4()))
    userId: str
    eventType: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    payload: Dict[str, Any] = {}