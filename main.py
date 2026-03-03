import asyncio
from Scrappers.hackernews import HackerNewsScraper
from Scrappers.reditt import RedditScraper
from Scrappers.fakestore import FakeStoreScraper
from utils.exporter import export_to_csv

async def main():
    hn = HackerNewsScraper()
    rd = RedditScraper()
    fs = FakeStoreScraper()

    results = await asyncio.gather(
        hn.scrape(),
        rd.scrape(),
        fs.scrape()
    )

    combined = [item for sublist in results for item in sublist]
    export_to_csv(combined)

    await hn.close()
    await rd.close()
    await fs.close()

if __name__ == "__main__":
    asyncio.run(main())
