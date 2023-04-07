import json 
from kafka import KafkaConsumer
from cassandra.cluster import Cluster, Session
from confluent_kafka import Consumer
from  article import Article

#pour lancer la console kafka : docker exec -it kafka /bin/sh 
#kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic article-ingest --from-beginning

#lister les topics : kafka-topics.sh --list --zookeeper zookeeper:2181

def save(article: Article, connection: Session, user_id: str):
        connection.execute(
            "INSERT INTO project.article (feed_id, article_id, title, pubDate, description, link) VALUES (%s, %s, %s, %s, %s, %s);",
            (article.feed_id, article.article_id, article.title, article.pubDate, article.description, article.link)
        )
        # row = connection.execute(
        #      "SELECT feed_id FROM project.feed WHERE feed_id = " + article.feed_id).one()
        # if row is None:
        #      connection.execute(
        #           "INSERT INTO project.feed (feed_id) VALUES (%s);",
        #           (article.feed_id)
        #      )
        connection.execute(
            "INSERT INTO project.feed (feed_id) VALUES (%s);",
            (article.feed_id)
        )
        # row = connection.execute(
        #      "SELECT user_id FROM project.user_id WHERE user_id = " + user_id).one()
        # if row is None:
        connection.execute(
            "INSERT INTO project.user (user_id) VALUES (%s);",
            (user_id)
        )
        connection.execute(
            "INSERT INTO project.user_feed (user_id, feed_id) VALUES (%s, %s);",
            (user_id, article.feed_id)
        )
        

             
            
        
if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'flux_rss',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    cluster = Cluster()

    try:
        connection = cluster.connect()

        for article in consumer:
            JsonArticle = json.loads(article.value)
            value = JsonArticle
            article = Article(feed_id=value['feed_id'], article_id=value['article_id'], title=value['title'], pubDate=value['pubDate'], description=value['description'], link=value['link'])
            save(article, connection, value['user_id'])


    finally:
        cluster.shutdown()
        consumer.close()
