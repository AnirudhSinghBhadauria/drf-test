import requests

endpoint = 'http://localhost:8000/'

# res = requests.post(postEndpoint, json={
#     "name": "Anirudh",
#     "middle": "Singh",
#     "last": "Bhadauria"
# })

# res = requests.get(endpoint)

res = requests.get(endpoint)
print(res.json())