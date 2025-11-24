from .ticker_service import TickerFinder
from .yahoo_service import YahooData
from .news_service import NewsFetcher
from .wiki_service import WikiFetcher
from .llm_client import LLMClient
from plan.plan_generator import PlanGenerator
from utils.text_cleaner import clean_text

class ResearchEngine:

    def __init__(self):
        self.ticker_finder = TickerFinder()
        self.yahoo = YahooData()
        self.news = NewsFetcher()
        self.wiki = WikiFetcher()
        self.llm = LLMClient()
        self.generator = PlanGenerator()

    def run(self, company: str):
        result = {
            "company": company,
            "ticker": None,
            "yahoo": None,
            "news": None,
            "wiki": None,
        }

        # Ticker finder
        ticker = self.ticker_finder.find_ticker(company)
        result["ticker"] = ticker

        if not ticker:
            fallback = self.llm.fallback_company_search(company)
            if fallback:
                result["wiki"] = fallback
            else:
                raise Exception("Company not found. Please provide a valid company name.")
        else:
            result["yahoo"] = self.yahoo.get_company_profile(ticker)
            result["news"] = self.news.get_news(company)
            result["wiki"] = self.wiki.get_wikipedia_summary(company)

        # Generate plan
        combined = {
            "yahoo": result["yahoo"],
            "news": result["news"],
            "wiki": result["wiki"]
        }

        plan = self.generator.generate(company, combined)

        # Clean
        cleaned = {key: clean_text(val) for key, val in plan.items()}

        return {
            "company": company,
            "ticker": ticker,
            "yahoo": result["yahoo"],
            "news": result["news"],
            "wiki": result["wiki"],
            "plan": cleaned
        }
