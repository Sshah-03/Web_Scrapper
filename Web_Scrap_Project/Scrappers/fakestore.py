import json
from Scrappers.base_scrappers import BaseScraper
from Models.data_models import NewsItem

class FakeStoreScraper(BaseScraper):

    async def scrape(self):
        url = "https://fakestoreapi.com/products"
        data = await self.fetch(url)
        products = json.loads(data)[:10]

        items = []
        for product in products:
            item = NewsItem(
                source="FakeStore",
                title=product.get("title"),
                url=None,
                score=int(product.get("rating", {}).get("rate", 0))
            )
            items.append(item)
        return items
