from typing import Dict
from app.models import UserEvent

class EventStore:
    def __init__(self):
        self.events: Dict[str, UserEvent] = {}

    def add_event(self, event: UserEvent) -> bool:
        """Returns True if new event, False if duplicate"""
        if event.eventId in self.events:
            return False
        self.events[event.eventId] = event
        return True

    def get_all(self):
        return list(self.events.values())

event_store = EventStore()