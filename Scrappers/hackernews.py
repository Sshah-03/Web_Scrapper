import json
from Scrappers.base_scrappers import BaseScraper
from Models.data_models import NewsItem

class HackerNewsScraper(BaseScraper):

    async def scrape(self):
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        data = await self.fetch(url)
        ids = json.loads(data)[:10]

        items = []
        for story_id in ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_data = await self.fetch(story_url)
            story = json.loads(story_data)

            item = NewsItem(
                source="HackerNews",
                title=story.get("title"),
                url=story.get("url"),
                score=story.get("score")
            )
            items.append(item)
        return items
