import requests

ENDPOINT = "http://127.0.0.1:8000/api/auth/login/"

response = requests.post(
    ENDPOINT,
    data={"username": "minasedr", "password": "123"},
    timeout=5,
)

print(response.json())
token = response.json().get("access")

ENDPOINT = "http://127.0.0.1:8000/api/auth/"

headers = {"AUTHORIZATION": f"Token {token}"}
resposne = requests.get(
    ENDPOINT,
    headers=headers,
    timeout=5,
)
print(response.json())
