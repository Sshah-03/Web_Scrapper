import httpx
import asyncio


class RedditScraper:

    async def fetch(self):

        await asyncio.sleep(2)

        url = "https://api.reddit.com/r/python"

        headers = {
            "User-Agent": "python:web_scraper_project:v1.0"
        }

        posts = []

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, headers=headers)

        data = response.json()

        children = data.get("data", {}).get("children", [])

        for post in children[:10]:

            post_data = post.get("data", {})

            posts.append({
                "title": post_data.get("title"),
                "url": post_data.get(
                    "url",
                    "https://reddit.com" + post_data.get("permalink", "")
                ),
                "description": post_data.get("selftext", "")[:120],
                "image": "",
                "price": ""
            })

        return posts
