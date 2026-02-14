from fastapi import APIRouter, HTTPException
from app.models import UserEventRequest, UserEvent
from app.producer import publish_event
from app.store import event_store

router = APIRouter()

@router.post("/events/generate", status_code=201)
async def generate_event(req: UserEventRequest):
    try:
        event = UserEvent(**req.dict())
        await publish_event(event.dict())
        return {"eventId": event.eventId}
    except Exception:
        raise HTTPException(500, "Failed to publish event")


@router.get("/events/processed")
async def get_processed():
    return event_store.get_all()