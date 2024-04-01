"""Admin-Client to create a new topic in Kafka."""
from kafka.admin import (
    KafkaAdminClient,
    NewTopic,
)

BOOTSTRAP_SERVERS = 'localhost:9092'
admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)

TOPIC_NAME = 'channels'

topic = NewTopic(name=TOPIC_NAME, num_partitions=1, replication_factor=1)
admin_client.create_topics([topic])

print(f"Topic {TOPIC_NAME} created.")

admin_client.close()
