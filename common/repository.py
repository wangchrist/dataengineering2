from typing import *

from cassandra.cluster import Session

from common import config
from common.article import Article, ArticleSummary


class ArticleRepository(object):
    def __init__(self, connection: Session):
        self.__connection = connection


    def findOneArticle(self, article_id: str) -> Optional[Article]:
        row = self.__connection.execute(
            "SELECT feed_id, title, pubDate, description, link FROM " + config.cassandra_table + " WHERE article_id = %s",
            (article_id,)
        ).one()

        if row is None:
            return None
        else:
            (feed_id, article_id, title, pubDate, description, link) = row
            return Article(feed_id=feed_id, article_id=article_id, title=title, pubDate=pubDate, description=description, link=link)


    def findLast10ArticleSummaries(self, user_id: str) -> List[ArticleSummary]:
        rows = self.__connection.execute(
            "SELECT feed_id, article_id, title, pubDate FROM " + config.cassandra_table + " ORDER BY pubDate DESC LIMIT 10"
            #faire requête prenant en compte l'user id
        ).all()

        result = []
        for (feed_id, article_id, title, pubDate) in rows:
            result.append(ArticleSummary(feed_id=feed_id, article_id=article_id, title=title, pubDate=pubDate))

        return result


    def saveArticles(self, articles: List[Article]):
        for article in articles:
            self.__connection.execute(
                "INSERT INTO " + config.cassandra_table + " (feed_id, article_id, title, pubDate, description, link) VALUES (%s, %s, %s, %s, %s, %s);",
                (article.feed_id, article.article_id, article.title, article.pubDate, article.description, article.link)
            )
