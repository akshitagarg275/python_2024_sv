import requests

res = requests.get("https://randomuser.me/api")

# print(res)

if res.status_code == 200:
    data = res.json()
    print(data["results"][0]["name"]["first"])
else:
    print("Failed to retrieve data: ", res.status_code)
