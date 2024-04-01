# Kafka with python.

### Quickstart:

#### __follow run commnad__:

    docker run --volume /your/path/:/mnt/shared/config -p 9092:9092 apache/kafka

#### __create virtual enviroment__:
    
    virtualenv .env

#### __Installed__:
    
    pip install kafka-python 

In the example folder, there are three modules (kafka_admin, consumer, and producer).

- kafka_admin.py: script create topic 'channels'.  
- consumer.py: script wait events or menssages.  
- producer.py: script create events or menssages.  

Open three terminals and run the scripts in the following order.
1. python kafka-admin.py (created topics channels.)  
2. python consumer.py (listening event or messages.)  
3. python producer.py (generate event or messages.)
