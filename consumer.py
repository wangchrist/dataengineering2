import json 
from kafka import KafkaConsumer

#pour lancer la console kafka : docker exec -it kafka /bin/sh 
#kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic article-ingest --from-beginning
#bin/kafka-topics --list --bootstrap-server localhost:9092

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'article-ingest',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for article in consumer:
        print(json.loads(article.value))

