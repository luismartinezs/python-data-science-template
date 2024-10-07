"""
third party libs

pip install package_name

eg

pip install requests

check if installed

pip list
"""

# GET
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
print(response.json())

url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Bitcoin price (USD): {data['bpi']['USD']['rate']}")
else:
    print("Failed to fetch data")

# POST
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "New Post", "body": "This is the body of the post.", "userId": 1}

response = requests.post(url, json=data)
print(response.status_code)  # Should return 201 for success
print(response.json())  # Response data from the server

# HEADERS AND PARAMS
params = {"q": "python programming", "sort": "relevance"}
headers = {"Authorization": "Bearer your_access_token"}

try:
    response = requests.get(
        "https://api.example.com/search", headers=headers, params=params
    )
    print(response.url)  # Prints the full URL with query params
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# ERROR HANDLING

try:
    response = requests.get("https://api.nonexistent.com/data")
    response.raise_for_status()  # Will raise an HTTPError for bad responses
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.ConnectionError:
    print("Error connecting to the server")
except Exception as e:
    print(f"An error occurred: {e}")
