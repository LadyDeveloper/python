import requests
from datetime import datetime

USERNAME = "ladydeveloper"
PASSWORD = "f&*@15jku"

APP_ID  = "1e8932ef"
API_KEY  = "aa67e7aa6094d70452bb5e1e9fefde68"

HEADERS  = {
    # "Authorization": "Basic bnVsbDpudWxs",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("Tell me what you did: ")

parameters = {
    "query": user_input
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url, headers=HEADERS, json=parameters)

result = response.json()


date = datetime.now()

for exercise in result['exercises']:
    body = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_url = 'https://api.sheety.co/eaebc8a61cc37e7434c358a0eb63c874/myWorkouts/workouts'

sheety_response = requests.post(sheety_url, json=body, auth=(USERNAME, PASSWORD))
print(sheety_response.status_code)
print(sheety_response.json)