from app.services.scraper_service import ScraperService


class ScraperController:

    def __init__(self):
        self.service = ScraperService()

    async def scrape(self, source):
        data = await self.service.scrape(source)
        return data
