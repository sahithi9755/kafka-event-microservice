import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"
)

KAFKA_TOPIC = os.getenv(
    "KAFKA_TOPIC", "user-activity-events"
)

CONSUMER_GROUP = os.getenv(
    "CONSUMER_GROUP", "user-activity-consumer-group"
)