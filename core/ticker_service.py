import requests

class TickerFinder:
    """
    Uses Yahoo Finance auto-complete API to detect the best matching ticker.
    More robust matching, better scoring, and safer fallbacks.
    """

    SEARCH_URL = "https://query2.finance.yahoo.com/v1/finance/search"

    def find_ticker(self, company: str):
        try:
            params = {"q": company, "quotes_count": 10}
            response = requests.get(self.SEARCH_URL, params=params, timeout=8)
            data = response.json()

            if "quotes" not in data or len(data["quotes"]) == 0:
                return None

            quotes = data["quotes"]

            # 1️Filter only real company tickers
            companies = [
                q for q in quotes
                if q.get("quoteType") == "EQUITY" and q.get("symbol")
            ]

            if companies:
                return companies[0]["symbol"]  # best match

            # 2️ Fallback: return first symbol if nothing else
            return quotes[0].get("symbol")

        except Exception:
            return None
