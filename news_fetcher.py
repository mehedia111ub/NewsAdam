import feedparser

NEWS_SOURCES = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html"
}

def fetch_news(topic=None, max_articles=10):
    articles = []

    for source, url in NEWS_SOURCES.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title
            summary = entry.get("summary", "")
            link = entry.link
            article = {"source": source, "title": title, "summary": summary, "link": link}

            if topic:
                if topic.lower() in title.lower() or topic.lower() in summary.lower():
                    articles.append(article)
            else:
                articles.append(article)

            if len(articles) >= max_articles:
                return articles
    return articles

def combine_articles(articles):
    text = ""
    for article in articles:
        text += article["title"] + "\n"
        text += article["summary"] + "\n\n"
    return text
