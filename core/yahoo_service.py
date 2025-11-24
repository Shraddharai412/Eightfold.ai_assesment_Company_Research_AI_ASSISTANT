import yfinance as yf

class YahooData:
    """
    Modern, stable Yahoo Finance fetcher using the updated yfinance endpoints.
    """

    def get_company_profile(self, ticker: str):
        try:
            stock = yf.Ticker(ticker)

            # New API: safer and more complete
            info = stock.get_info()

            if not info:
                return None

            return {
                "longName": info.get("longName"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "marketCap": info.get("marketCap"),
                "employees": info.get("fullTimeEmployees"),
                "website": info.get("website"),
                "city": info.get("city"),
                "state": info.get("state"),
                "country": info.get("country"),
                "summary": info.get("longBusinessSummary"),

                # NEW ITEMS
                "currency": info.get("currency"),
                "exchange": info.get("exchange"),
                "quoteType": info.get("quoteType"),
                "dividendYield": info.get("dividendYield"),
                "priceToSales": info.get("priceToSalesTrailing12Months"),
                "priceToBook": info.get("priceToBook"),
            }

        except Exception:
            return None
