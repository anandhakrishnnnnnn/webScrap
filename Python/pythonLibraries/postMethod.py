#post method

import requests

data = {
   "Name":"Anandhakrishnan",
   "Batch":"BCE309"
}

response = requests.post("https://httpbin.org/post", data=data)

print(response.json())

