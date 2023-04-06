import json 
from ingest.scraping import scraping_feed
from kafka import KafkaProducer
from kafka.errors import KafkaError

import feedparser
import requests
import json

# def scraping_feed(url):

#     feed = feedparser.parse(url)

#     url = 'http://localhost:8888/articles'
#     headers = {'Content-Type': 'scraping_flux_RSS'}

#     for entry in feed.entries:
#         article = {
#             "title": entry.title,
#             "link": entry.link,
#             "pubDate": entry.published,
#             "description": entry.summary,
#             "guid": entry.id
#         }
#         requests.post(url, data=json.dumps(article), headers=headers)

def scraping_feed(url):
    # for url in urls:
    feed = feedparser.parse(url)
    articles =[]

    for entry in feed.entries:
        article = {
            "title": entry.title,
            "link": entry.link,
            "pubDate": entry.published,
            "description": entry.summary,
            "guid": entry.id
        }
        articles.append(article)
    return articles

# On crée le Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
)

if __name__ == '__main__':
    # urls = [
    # # "https://www.linux-magazine.com/rss/feed/lmi_news",
    # # "https://www.lemonde.fr/sciences/rss_full.xml",
    # # "https://www.lemonde.fr/rss/une.xml",
    # "https://www.cert.ssi.gouv.fr/alerte/feed/" 
    # ]
    url = "https://www.cert.ssi.gouv.fr/alerte/feed/"
    #On appelle la fonction qui permet de scrapper les feeds 
    articles = scraping_feed(url)
    print(articles)

    #on envoie chaque article dans le producer kafka pour les stocker
    for article in articles:
        try:
            producer.send('article-ingest', key=article['title'].encode(), value=json.dumps(article).encode())
        except KafkaError as e:
            print(f"Failed to send message to Kafka: {e}")
        producer.flush()