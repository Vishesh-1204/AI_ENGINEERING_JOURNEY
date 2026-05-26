import requests
url="https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "tether",
    "vs_currencies": "inr"
}
response = requests.get(url, params=params,timeout=5)
print(response.status_code)
print(response.json())

try:

    response = requests.get("https://api.github.com", 
                            params=params,
                            timeout=5)
    print(response.status_code)
    print(response.json())
except:
    print("something went wrong")

 