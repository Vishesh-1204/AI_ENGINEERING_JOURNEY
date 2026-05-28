import aiohttp
import asyncio

async def fetch():

    url = "https://api.github.com"

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            data = await response.json()

            print(data)

asyncio.run(fetch())