import requests

url = "http://localhost:5000/generate"

data = {"prompt":  "Explain dark mode UI"}

res = requests.post(url, json=data)

print("Status Code:", res.status_code)

print(res.json())