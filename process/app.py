import json
import time
from typing import *

from cassandra.cluster import Cluster, Session
from confluent_kafka import Consumer

from common import config
from common.article import Article


class ArticleConsumer(object):
    def __init__(self, consumer: Consumer, topic: str):
        self.__consumer = consumer
        self.__consumer.subscribe([topic])

    def next_article(self) -> Optional[Article]:
        message = consumer.poll(0.5)
        if message is None:
            return None
        elif message.error():
            print("Error: %s" % message.error().str())
            return None
        else:
            key = message.key().decode("utf-8")
            value = json.loads(message.value().decode("utf-8"))

            return Article(feed_id=value['feed_id'], article_id=key, title=value['title'], pubDate=value['pubDate'], description=value['description'], link=value['link'])


class ArticleRepository(object):
    def __init__(self, connection: Session):
        self.__connection = connection

    def saveArticles(self, articles: List[Article]):
        for article in articles:
            self.__connection.execute(
                "INSERT INTO " + config.cassandra_table + " (feed_id, article_id, title, pubDate, description, link) VALUES (%s, %s, %s, %s, %s, %s);",
                (article.feed_id, article.article_id, article.title, article.pubDate, article.description, article.link)
            )


class ProcessService(object):
    def __init__(self, consumer: ArticleConsumer, connection: ArticleRepository):
        self.__consumer = consumer
        self.__connection = connection

    def get_and_save_article(self):
        article = self.__consumer.next_article()
        if article is not None:
            self.__connection.save(article)


if __name__ == '__main__':
    article_topic = config.ingestTopic
    article_keyspace = "store"
    group_id = "process-group-0"

    consumer = Consumer({
        'bootstrap.servers': config.kafkaHost,
        'group.id': group_id,
        'default.topic.config': {'auto.offset.reset': 'earliest'}
    })

    cluster = Cluster()

    try:
        connection = cluster.connect()

        article_repository = ArticleRepository(connection)
        article_consumer = ArticleConsumer(consumer, article_topic)
        service = ProcessService(article_consumer, article_repository)

        while True:
            service.get_and_save_article()

    finally:
        cluster.shutdown()
        consumer.close()
