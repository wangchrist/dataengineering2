import feedparser
import requests
import json
def scraping_feed(url):
    
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
    url = 'http://localhost:8888/articles'
    headers = {'Content-Type': 'scraping_flux_RSS'}
    return requests.post(url, data=json.dumps(articles), headers=headers)
