import json
import httpx
from Scrappers.base_scrappers import BaseScraper
from Models.data_models import NewsItem
from Core.logger import setup_logger

logger = setup_logger()

class RedditScraper(BaseScraper):

    async def scrape(self):
        url = "https://www.reddit.com/r/python/top.json?limit=10"
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; EnterpriseScraper/1.0)"
        }

        try:
            response = await self.client.get(url, headers=headers)

            logger.info(f"Reddit status code: {response.status_code}")

            response.raise_for_status()

            if not response.text.strip():
                logger.error("Empty response from Reddit")
                return []

            data = response.json()

            posts = data.get("data", {}).get("children", [])

            items = []
            for post in posts:
                p = post["data"]

                item = NewsItem(
                    source="Reddit",
                    title=p.get("title"),
                    url=p.get("url"),
                    score=p.get("score")
                )
                items.append(item)

            return items

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error while scraping Reddit: {e}")
            return []

        except json.JSONDecodeError:
            logger.error("Failed to decode Reddit JSON response")
            return []

        except Exception as e:
            logger.error(f"Unexpected Reddit scraping error: {e}")
            return []