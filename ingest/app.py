from http import HTTPStatus

from scraping import scraping_feed
from confluent_kafka import Producer
from flask import Flask, request, Response
from flask_classful import FlaskView, route

from common.config import ingestTopic, ingestPort, kafkaHost
from common.article import Article

import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

class ArticleProducer(object):
    def __init__(self, producer: Producer, topic: str):
        self.__producer = producer
        self.__topic = topic

    def send(self, article: Article):
        self.__producer.produce(topic=self.__topic, key=article.article_id, value=article.toJson())
        self.__producer.flush(0.5)


class IngestView(FlaskView):
    producer: ArticleProducer = None

    
    @route("/articles/<article_id>", methods=['POST'])
    def article(self, article_id):
        feed_id = request.json['feed_id']
        article_id = request.json['article_id']
        title = request.json['title']
        pubDate = request.json['pubDate']
        description = request.json['description']
        link = request.json['link']
        article = Article(feed_id=feed_id, article_id=article_id, title=title, pubDate=pubDate, description=description, link=link)
        print("ingesting article: %s" % article)
        self.__class__.producer.send(article)

        return Response(status=HTTPStatus.OK)
    
    # @route("/articles/", methods=['POST'])
    # def article(self, article_id):
    #     feed_id = request.json['feed_id']
    #     article_id = request.json['article_id']
    #     title = request.json['title']
    #     pubDate = request.json['pubDate']
    #     description = request.json['description']
    #     link = request.json['link']
    #     article = Article(feed_id=feed_id, article_id=article_id, title=title, pubDate=pubDate, description=description, link=link)
    #     print("ingesting article: %s" % article)
    #     self.__class__.producer.send(article)

    #     return Response(status=HTTPStatus.OK)


def main():
    topic = ingestTopic
    port = ingestPort
    route_base = "/api"

    producer = Producer({'bootstrap.servers': kafkaHost})
    IngestView.producer = ArticleProducer(producer, topic)

    app = Flask(__name__)
    IngestView.register(app, route_base=route_base)
    app.run("0.0.0.0", port, debug=True)

if __name__ == '__main__':
    url = "https://www.cert.ssi.gouv.fr/alerte/feed/"
    scraping_feed(url)

    main()
