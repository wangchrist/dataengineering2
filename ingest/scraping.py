import feedparser
import requests
import json
def scraping_feed(url):

    feed = feedparser.parse(url)

    url = 'http://localhost:8888/articles'
    headers = {'Content-Type': 'scraping_flux_RSS'}

    for entry in feed.entries:
        article = {
            "title": entry.title,
            "link": entry.link,
            "pubDate": entry.published,
            "description": entry.summary,
            "guid": entry.id
        }
        requests.post(url, data=json.dumps(article), headers=headers)