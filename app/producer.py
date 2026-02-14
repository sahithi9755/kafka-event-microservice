import json
import asyncio
from aiokafka import AIOKafkaProducer
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

producer = None

async def start_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        acks="all",
        linger_ms=10,
    )
    await producer.start()

async def stop_producer():
    await producer.stop()

async def publish_event(event_dict: dict):
    try:
        await producer.send_and_wait(
            KAFKA_TOPIC,
            json.dumps(event_dict).encode("utf-8")
        )
    except Exception as e:
        print(f"❌ Producer error: {e}")
        raise