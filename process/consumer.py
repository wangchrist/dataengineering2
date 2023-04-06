import json 
from kafka import KafkaConsumer
from common.repository import Article
from common.config import cassandra_table
from cassandra.cluster import Cluster, Session
from confluent_kafka import Consumer

#pour lancer la console kafka : docker exec -it kafka /bin/sh 
#kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic article-ingest --from-beginning
#bin/kafka-topics --list --bootstrap-server localhost:9092

def save(article: Article, connection: Session):
        connection.execute(
            "INSERT INTO " + cassandra_table + " (feed_id, article_id, title, pubDate, description, link) VALUES (%s, %s, %s, %s, %s, %s);",
            (article.feed_id, article.article_id, article.title, article.pubDate, article.description, article.link)
        )

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'article-ingest',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )    
    
    cluster = Cluster()

    try:
        connection = cluster.connect()

        for article in consumer:
            # print(json.loads(article.value))
            message = consumer.poll(0.5)
            key = message.key().decode("utf-8")
            value = json.loads(message.value().decode("utf-8"))
            article = Article(feed_id=value['feed_id'], article_id=key, title=value['title'], pubDate=value['pubDate'], description=value['description'], link=value['link'])
            save(article, connection)

    finally:
        cluster.shutdown()
        consumer.close()

   
        


