import requests
from config import api_token, username
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = username
TOKEN = api_token

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "My Programming Graph",
    "unit": "Hr",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

fill_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params.get('id')}"

today = datetime.now()
# print(today)

fill_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=fill_pixel, json=fill_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = f"{fill_pixel}/20210122"

response = requests.put(url=delete_endpoint, headers=headers)
print(response.text)