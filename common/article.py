import json


class Article(object):
    feed_id: str
    article_id: str
    title: str
    pubDate: str
    description: str
    link: str
    

    def __init__(self, feed_id: str, article_id: str, title: str, pubDate: str, description: str, link: str):
        self.feed_id = feed_id
        self.article_id = article_id
        self.title = title
        self.pubDate = pubDate
        self.description = description
        self.link = link

    def __str__(self):
        return "%s(%s,%s)" % (self.__class__.__name__, self.id, self.quantity)

    def toDict(self):
        return {'feed_id': self.feed_id, 'article_id': self.article_id, 'title': self.title, 'pubDate': self.pubDate, 'description': self.description, 'link': self.link}

    def toJson(self):
        return json.dumps(self.toDict())



class ArticleSummary(object):
    feed_id: str
    article_id: str
    title: str
    pubDate: str #datetime plutot ?
    

    def __init__(self, feed_id: str, article_id: str, title: str, pubDate: str):
        self.feed_id = feed_id
        self.article_id = article_id
        self.title = title
        self.pubDate = pubDate

    def __str__(self):
        return "%s(%s,%s)" % (self.__class__.__name__, self.id, self.quantity)

    def toDict(self):
        return {'feed_id': self.feed_id, 'article_id': self.article_id, 'title': self.title, 'pubDate': self.pubDate}

    def toJson(self):
        return json.dumps(self.toDict())
