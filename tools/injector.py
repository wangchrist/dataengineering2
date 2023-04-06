import requests

from common.article import Article
from common import config

import random
import time

#créer des articles random ??? 

class ArticleSender(object):
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port

    def send(self, article: Article):
        data = article.toJson()
        response = requests.post(
            "http://%s:%s/api/aricles/%s" % (self.__host, self.__port, article.article_id),
            json=data
        )
        try:
            print("Sent with %s %s: %s" % (response.status_code, response.reason, data))
        finally:
            response.close()


if __name__ == '__main__':
    article_ids = range(0, 20)
    host = "localhost"
    port = config.ingestPort

    sender = ArticleSender(host, port)

    while True:
        id = str(random.choice(article_ids))
        quantity = random.randint(1, 100)
        article = Article(id=id, quantity=quantity)
        sender.send(article)
        time.sleep(1)