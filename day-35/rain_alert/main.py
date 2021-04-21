import requests
from twilio.rest import Client


account_sid ="ACdfefee402711a051b1f4b3141a879ffa"
auth_token = "f10181b1a6830c46f581b745a04bf5ce"



url = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "60a4615d1ae621d4fe3c137934e1ef02"

parameters = {
"lat": -15.826691,
"lon": -47.921822,
"exclude": "current,minutely,daily",
"appid":  api_key, 
}

response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json() 
#print(weather_data)

for hour in range(12):
    id_weather = weather_data['hourly'][hour]['weather'][0]['id']
    if id_weather < 700:
        print('Bring an umbrella')



# Angela solution 
will_rain = False
weather_slice = weather_data['hourly'][:11]
for hour_data in weather_slice:
    conditiion_code = hour_data['weather'][0]['id']
    if int(conditiion_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)   
    message = client.messages \
                .create(
                     body="Bring an umbrella because it is gonna rain today!☔☔☔☔",
                     from_='+16193562614',
                     to='+17022046034'
                 )
    print(message.status)
