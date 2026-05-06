import requests

url = "http://localhost:5000/generate"

data = {"prompt":"Explain dark mode UI"}

res = requests.post(url, json=data)

print(res.json())