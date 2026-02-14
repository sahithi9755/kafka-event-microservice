from app.models import UserEvent

def test_event_creation():
    """
    Unit test to verify UserEvent is created correctly.
    Ensures required fields are auto-generated.
    """
    event = UserEvent(
        userId="user1",
        eventType="LOGIN",
        payload={}
    )

    # verify fields
    assert event.userId == "user1"
    assert event.eventType == "LOGIN"
    assert event.eventId is not None
    assert event.timestamp is not None