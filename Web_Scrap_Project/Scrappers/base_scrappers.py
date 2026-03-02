import httpx
from Core.cache import CacheManager
from Core.rate_limiter import rate_limiter
from Core.retry import retry_strategy
from Core.logger import setup_logger
from config import REQUEST_TIMEOUT

logger = setup_logger()

class BaseScraper:

    def __init__(self):
        self.cache = CacheManager()
        self.client = httpx.AsyncClient(timeout=REQUEST_TIMEOUT)

    @retry_strategy()
    @rate_limiter()
    async def fetch(self, url):
        cached = self.cache.get(url)
        if cached:
            logger.info(f"Cache hit for {url}")
            return cached

        logger.info(f"Fetching {url}")
        response = await self.client.get(url)
        response.raise_for_status()

        self.cache.set(url, response.text)
        return response.text

    async def close(self):
        await self.client.aclose()
