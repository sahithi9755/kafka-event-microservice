import asyncio
import httpx

BASE_URL = "http://app:8000"

def test_end_to_end():
    async def run_test():
        async with httpx.AsyncClient() as client:
            payload = {
                "userId": "u1",
                "eventType": "LOGIN",
                "payload": {}
            }

            r = await client.post(f"{BASE_URL}/events/generate", json=payload)
            assert r.status_code == 201

            await asyncio.sleep(5)

            r = await client.get(f"{BASE_URL}/events/processed")
            assert r.status_code == 200
            assert len(r.json()) >= 1

    asyncio.run(run_test())