import requests

while True:

    coin = input("Enter coin name: ")

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if coin in data:

            usd = data[coin]["usd"]
            inr = data[coin]["inr"]

            print(f"{coin.upper()} Price")
            print(f"USD: ${usd}")
            print(f"INR: ₹{inr}")

        else:
            print("Invalid coin name")

    else:
        print("API Error")