import requests
import pandas as pd
# Get Data from API
url="https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
response.raise_for_status()

#Convert JSON to DataFrame
data = response.json()
df = pd.DataFrame(data)
print("Original DataFrame")
print(df.head())

#check missing values
print("/nMissing Values:")
print(df.isna().sum())
