import feedparser


def scraping_feed(urls):
    for url in urls:
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





       
