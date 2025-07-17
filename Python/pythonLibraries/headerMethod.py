import requests

headers = {
    "User-Agent": "anandhan-security-bot",
    "Accept": "application/json"
}

response = requests.get("https://httpbin.org/headers", headers=headers)

print(response.json())
