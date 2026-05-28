import aiohttp
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

weather_key = os.getenv("WEATHER_API")
news_key = os.getenv("NEWS_API")


coin = input("Enter crypto coin: ").lower()
city = input("Enter city name: ")
topic = input("Enter news topic: ")


async def get_crypto(session):

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    async with session.get(url) as response:

        data = await response.json()

        if coin in data:

            return f"{coin.upper()} Price: ${data[coin]['usd']}"

        return "Invalid crypto coin"


async def get_weather(session):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"

    async with session.get(url) as response:

        data = await response.json()

        if "main" in data:

            temp = data['main']['temp']

            return f"{city} Temperature: {temp}°C"

        return f"Weather Error: {data.get('message')}"


async def get_news(session):

    url = f"http://api.mediastack.com/v1/news?access_key={news_key}&keywords={topic}"

    async with session.get(url) as response:

        data = await response.json()

        if "data" in data and len(data["data"]) > 0:

            return f"Top News on {topic}: {data['data'][0]['title']}"

        return "No news found"


async def main():

    async with aiohttp.ClientSession() as session:

        results = await asyncio.gather(
            get_crypto(session),
            get_weather(session),
            get_news(session)
        )

        print("\n===== DASHBOARD =====\n")

        for result in results:

            print(result)


asyncio.run(main())