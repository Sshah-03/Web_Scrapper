from app.scrapers.reddit_scraper import RedditScraper
from app.scrapers.hackernews_scraper import HackerNewsScraper
from app.scrapers.fakestore_scraper import FakeStoreScraper

from app.utils.cache_manager import CacheManager
from app.utils.concurrent_runner import ConcurrentRunner


class ScraperService:

    def __init__(self):

        self.cache = CacheManager()
        self.runner = ConcurrentRunner()

    async def scrape(self, source):

        cached = self.cache.get(source)

        if cached:
            return cached

        if source == "reddit":
            scrapers = [RedditScraper()]

        elif source == "hackernews":
            scrapers = [HackerNewsScraper()]

        elif source == "fakestore":
            scrapers = [FakeStoreScraper()]

        elif source == "all":
            scrapers = [
                RedditScraper(),
                HackerNewsScraper(),
                FakeStoreScraper()
            ]

        else:
            return []

        results = await self.runner.run(scrapers)

        self.cache.set(source, results)

        return results
