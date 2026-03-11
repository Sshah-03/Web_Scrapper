import httpx


class FakeStoreScraper:

    async def fetch(self):

        url = "https://fakestoreapi.com/products"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        products = response.json()

        results = []

        for p in products[:10]:

            results.append({
                "title": p.get("title"),
                "url": f"https://fakestoreapi.com/products/{p.get('id')}",
                "description": p.get("description"),
                "image": p.get("image"),
                "price": p.get("price")
            })

        return results
