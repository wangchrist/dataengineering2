import json 
import random
import string
from kafka import KafkaProducer
from kafka.errors import KafkaError
from datetime import datetime
import feedparser

import json


def scraping_feed(url):
    # for url in urls:
    feed = feedparser.parse(url)
    rss_id =  ''.join(random.choice(string.ascii_letters) for i in range(32))
    articles =[]

    for entry in feed.entries:
        article = {
            "feed_id": rss_id ,
            "title": entry.title,
            "link": entry.link,
            "pubDate": datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d'),
            "description": entry.summary,
            "article_id": entry.id
        }
        articles.append(article)
    return articles


# On crée le Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
)

def send_to_producer(url):
    articles = scraping_feed(url)

    #on envoie chaque article dans le producer kafka pour les stocker
    for article in articles:
        try:
            producer.send('flux_rss', key = article['article_id'].encode(), value=json.dumps(article).encode())
        except KafkaError as e:
            print(f"Failed to send message to Kafka: {e}")
        producer.flush()

# if __name__ == '__main__':

    # url = "https://www.cert.ssi.gouv.fr/alerte/feed/"
    # #On appelle la fonction qui permet de scrapper les feeds 
    # articles = scraping_feed(url)


    # #on envoie chaque article dans le producer kafka pour les stocker
    # for article in articles:
    #     try:
    #         producer.send('flux_rss', key = article['article_id'].encode(), value=json.dumps(article).encode())
    #     except KafkaError as e:
    #         print(f"Failed to send message to Kafka: {e}")
    #     producer.flush()
