# Kafka Event-Driven Microservice

## 📌 Overview

This project implements a foundational event-driven microservice using **FastAPI** and **Apache Kafka**.  
The service acts as both a Kafka **producer** and **consumer**, demonstrating asynchronous communication, idempotent processing, and containerized deployment.

This project showcases core concepts required for building scalable and resilient distributed backend systems.

---

## 🚀 Features

- REST API to generate user activity events
- Kafka producer publishes events to topic
- Kafka consumer processes events
- Idempotent event handling (no duplicate processing)
- In-memory storage of processed events
- Fully containerized using Docker Compose
- Health checks for Kafka and Zookeeper
- Unit and integration tests

---

## 🧱 Tech Stack

- Python 3.11
- FastAPI
- Apache Kafka
- Zookeeper
- Docker & Docker Compose
- Pytest

---

## 📂 Project Structure
kafka-event-microservice/
│
├── app/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sahithi9755/kafka-event-microservice.git
cd kafka-event-microservice
