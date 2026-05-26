import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MEDIASTACK_API_KEY")

keyword = input("Enter keyword: ")

url = "https://api.mediastack.com/v1/news"

params = {
    "access_key": api_key,
    "keywords": keyword,
    "languages": "en"
}

response = requests.get(url, params=params)

data = response.json()

articles = data["data"]

for article in articles[:5]:

    print(article["title"])