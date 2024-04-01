""" Module to send messages to Kafka. """
from kafka import KafkaProducer

producer = KafkaProducer()

for _ in range(100):
    producer.send('channels', b'Hola Mundo!!!')

producer.flush()
producer.close()
