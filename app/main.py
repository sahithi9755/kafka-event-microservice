import asyncio
from fastapi import FastAPI
from app.api import router
from app.producer import start_producer, stop_producer
from app.consumer import consume_events

app = FastAPI(title="Kafka Event Microservice")

app.include_router(router)

@app.on_event("startup")
async def startup():
    await start_producer()
    asyncio.create_task(consume_events())

@app.on_event("shutdown")
async def shutdown():
    await stop_producer()