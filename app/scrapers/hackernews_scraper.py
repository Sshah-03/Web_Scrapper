import httpx

class HackerNewsScraper:

    async def fetch(self):

        url = "https://hacker-news.firebaseio.com/v0/topstories.json"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        story_ids = response.json()[:10]

        stories = []

        async with httpx.AsyncClient() as client:
            for story_id in story_ids:

                story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

                res = await client.get(story_url)

                data = res.json()

                stories.append({
                    "title": data.get("title"),
                    "url": data.get("url"),
                    "description": "",
                    "image": "",
                    "price": ""
                })

        return stories
