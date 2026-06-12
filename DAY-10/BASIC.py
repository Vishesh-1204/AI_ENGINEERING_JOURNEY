import pandas as pd
data = {
    "Product": ["Laptop", "Phone"],
    "Sales": [1000, 500]
}

df = pd.DataFrame(data)

print(df)
print(df.shape())
df.info()
print(df.describe())
