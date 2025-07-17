# #post method

# import requests

# data = {
#    "Name":"Anandhakrishnan",
#    "Batch":"BCE309"
# }

# response = requests.post("https://httpbin.org/post", data=data)

# print(response.json())

import requests

# Step 1: Create the file if it doesn't exist
with open("test.txt", "w") as f:
    f.write("This is a test file created by Anandhan's script.")

# Step 2: Send it in a POST request
with open("test.txt", "rb") as file_data:
    files = {'file': file_data}
    response = requests.post("https://httpbin.org/post", files=files)

print(response.json())
