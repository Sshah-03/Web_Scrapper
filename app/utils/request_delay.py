import asyncio

class RequestDelay:

    async def wait(self):
        await asyncio.sleep(2)
