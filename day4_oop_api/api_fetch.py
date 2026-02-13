import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("API request failed:", e)
        return []


# data = fetch_users()
# print(data)S