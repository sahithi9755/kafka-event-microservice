from app.store import EventStore
from app.models import UserEvent

def test_idempotency():
    store = EventStore()

    event = UserEvent(
        eventId="123",
        userId="u1",
        eventType="LOGIN",
        payload={}
    )

    assert store.add_event(event) is True
    assert store.add_event(event) is False