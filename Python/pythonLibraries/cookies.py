import requests

cookies = {
    "sessionid": "fake123"
}

res = requests.get("https://httpbin.org/cookies", cookies=cookies)
print(res.json())
