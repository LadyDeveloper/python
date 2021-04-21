import requests
from datetime import datetime

MY_LAT = "115.1398"
MY_LONG = "36.1699"
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()

# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']

# iss_position = (longitude, latitude)
# print(type(iss_position))
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunset)

time_now = datetime.now()
print(time_now)