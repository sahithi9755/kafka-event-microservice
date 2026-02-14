# Kafka Event-Driven Microservice

## Overview

This project implements an event-driven microservice using FastAPI and Apache Kafka.  
The service acts as both a Kafka producer and consumer, demonstrating asynchronous communication and idempotent event processing.

## Features

- REST API to generate user events
- Kafka producer publishes events
- Kafka consumer processes events
- Idempotent event handling
- In-memory event storage
- Dockerized environment
- Unit and integration tests

## Tech Stack

- Python (FastAPI)
- Apache Kafka
- Zookeeper
- Docker & Docker Compose
- Pytest

## Setup

```bash
docker-compose up --build

---
## RUN Tests
---
docker-compose exec app pytest tests -v
---

# 💪 Seriously — great job under pressure

You debugged:

- Docker  
- Kafka  
- Async pytest  
- Python path issues  

That’s **real backend engineering work**.

---

If later you want to **upgrade this to senior-level production quality**, just come back and say:

> Upgrade this to production-grade 🚀