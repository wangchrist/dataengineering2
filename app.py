import json
from http import HTTPStatus

from cassandra.cluster import Cluster
from flask import Flask, Response
from flask_classful import FlaskView, route

from common import config
from common.repository import ArticleRepository


class ApiView(FlaskView):
    repository: ArticleRepository = None

    # @route("/stocks/_count", methods=['GET'])
    # def count_stocks(self):
    #     result = len(self.__class__.repository.find_all())

    #     return Response(json.dumps({'count': result}), mimetype="application/json")

    #récupérer les détails d'un article
    @route("/articles/<article_id>", methods=['GET'])
    def article(self, article_id: str):
        result = self.__class__.repository.findOneArticle(article_id)

        if result is None:
            return Response(json.dumps({'article_id': article_id, 'error': "not found"}), mimetype="application/json",
                            status=HTTPStatus.NOT_FOUND)
        else:
            return Response(json.dumps(result.toDict()), mimetype="application/json")

    #last 10 article summaries
    @route("/articles/articles?user_id=<user_id>", methods=['GET'])
    def last_10_articles_summaries(self, user_id: str):
        results = self.__class__.repository.findLast10ArticleSummaries(user_id)

        return Response(json.dumps([s.toDict() for s in results]), mimetype="application/json")


if __name__ == '__main__':
    port = config.apiPort

    cluster = Cluster()
    connection = cluster.connect()
    try:
        app = Flask(__name__)
        ApiView.repository = ArticleRepository(connection)
        ApiView.register(app, route_base="/api")
        app.run("0.0.0.0", port)
    finally:
        cluster.shutdown()
