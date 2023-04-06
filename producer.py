import json 
from scraping import scraping_feed
from kafka import KafkaProducer
from kafka.errors import KafkaError

# On crée le Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
)


if __name__ == '__main__':
    urls = [
    # "https://www.linux-magazine.com/rss/feed/lmi_news",
    # "https://www.lemonde.fr/sciences/rss_full.xml",
    # "https://www.lemonde.fr/rss/une.xml",
    "https://www.cert.ssi.gouv.fr/alerte/feed/" 
    ]
    #On appelle la fonction qui permet de scrapper les feeds 
    articles = scraping_feed(urls)
    print(articles)

    #on envoie chaque article dans le producer kafka pour les stocker
    for article in articles:
        try:
            producer.send('article-ingest', value=json.dumps(article).encode())
        except KafkaError as e:
            print(f"Failed to send message to Kafka: {e}")
        producer.flush()
    

