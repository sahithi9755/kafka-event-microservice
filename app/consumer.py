import json
import asyncio
from aiokafka import AIOKafkaConsumer
from app.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    CONSUMER_GROUP,
)
from app.store import event_store
from app.models import UserEvent

consumer = None

async def consume_events():
    global consumer
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=CONSUMER_GROUP,
        enable_auto_commit=True,
    )

    await consumer.start()
    print("✅ Consumer started")

    try:
        async for msg in consumer:
            try:
                data = json.loads(msg.value.decode())
                event = UserEvent(**data)

                is_new = event_store.add_event(event)

                if is_new:
                    print(
                        f"Processed: {event.eventId} | "
                        f"{event.userId} | {event.eventType}"
                    )
                else:
                    print(f"⚠️ Duplicate ignored: {event.eventId}")

            except Exception as e:
                print(f"❌ Consumer processing error: {e}")

    finally:
        await consumer.stop()