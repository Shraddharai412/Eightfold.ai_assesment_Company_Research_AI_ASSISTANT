import feedparser

GOOGLE_NEWS_URL = "https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

class NewsFetcher:
    """
    Fetches latest Google News headlines for the company.
    """

    def get_news(self, company: str, limit: int = 8):
        try:
            url = GOOGLE_NEWS_URL.format(query=company.replace(" ", "+"))
            feed = feedparser.parse(url)

            articles = []

            for entry in feed.entries[:limit]:
                published = (
                    getattr(entry, "published", None)
                    or getattr(entry, "updated", None)
                    or ""
                )

                articles.append({
                    "title": entry.title,
                    "link": entry.link,
                    "published": published,
                })

            return articles

        except Exception:
            return None
