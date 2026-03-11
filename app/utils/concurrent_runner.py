import asyncio

class ConcurrentRunner:

    async def run(self, scrapers):

        tasks = []

        for scraper in scrapers:
            tasks.append(scraper.fetch())

        results = await asyncio.gather(*tasks)

        combined = []

        for result in results:
            combined.extend(result)

        return combined
