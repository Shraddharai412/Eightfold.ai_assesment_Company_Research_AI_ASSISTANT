import wikipedia

class WikiFetcher:
    """
    Strong, stable Wikipedia fetcher with full error handling.
    """

    def get_wikipedia_summary(self, company: str):
        try:
            wikipedia.set_lang("en")

            # 1️ Search for best matching page
            search_results = wikipedia.search(company)
            if not search_results:
                return None

            best_title = search_results[0]

            # 2️ Fetch the page safely
            page = wikipedia.page(best_title, auto_suggest=False)

            return {
                "title": page.title,
                "summary": page.summary,
                "url": page.url,
                "content": page.content[:5000]
            }

        except wikipedia.exceptions.DisambiguationError as e:
            # Pick the first valid option
            try:
                page = wikipedia.page(e.options[0])
                return {
                    "title": page.title,
                    "summary": page.summary,
                    "url": page.url,
                    "content": page.content[:5000]
                }
            except:
                return None

        except wikipedia.exceptions.PageError:
            return None

        except Exception:
            return None
