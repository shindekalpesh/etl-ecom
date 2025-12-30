import requests
import pandas as pd
pd.set_option('display.max_columns', None)

# print("requests", type(requests), requests)

products_url = "https://fakestoreapi.com/products/"
products_response = requests.get(products_url)

print("products_response", type(products_response), products_response)

products_data = products_response.json()

print("\n\n")
print("products_response.json()[0]", '\n', products_response.json()[0])

products_df = pd.json_normalize(products_data)
print("products_df.shape", products_df.shape)
print("products_df.head()", type(products_df.head()), '\n', products_df.head())

