"""Module Consumer to receive messages from Kafka."""
from kafka import KafkaConsumer

consumer = KafkaConsumer('channels', bootstrap_servers='localhost:9092')
for msg in consumer:
    print(f'Topic: {msg.topic} --- Value: {msg.value.decode("utf-8")}')
