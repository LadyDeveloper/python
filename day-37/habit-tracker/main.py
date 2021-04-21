import requests
from datetime import datetime

USERNAME = "ladydeveloper"
TOKEN = "Ch@ngeTudoIn2021"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)

#After run post it has been created https://pixe.la/@ladydeveloper

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "coding",
    "name": "Python Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/coding"

today = datetime.now()

pixel_graph_graph = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}


# response = requests.post(url=pixel_graph_endpoint, headers=headers, json=pixel_graph_graph )
# print(response.text)

#Put/Update

date = datetime(year=2021 ,month=1, day=9)
date_formatted = date.strftime("%Y%m%d")

pixel_graph_update =  f"{pixela_endpoint}/{USERNAME}/graphs/coding/{date_formatted}"

pixel_graph_update_params = {
    "quantity": "0"
}

# response = requests.put(url=pixel_graph_update, json=pixel_graph_update_params, headers=headers)
# print(response.text)

date_delete = today.strftime("%Y%m%d")

pixel_graph_delete =  f"{pixela_endpoint}/{USERNAME}/graphs/coding/{date_delete}"

response = requests.delete(url=pixel_graph_delete, headers=headers)
print(response.text)
