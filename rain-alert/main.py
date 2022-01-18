import requests
from twilio.rest import Client
from config import api_key, account_sid, auth_token

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = api_key
account_sid = account_sid
auth_token = auth_token

weather_params = {
    "lat": 18.506395,
    "lon": 73.788760,
    "appid": api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    else:
        exit

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It going to rain today. Remeber to bring your umbrella ☔",
        from_='+19377447658',
        to='+918446487230'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It going to be sunny. Remember to bring your cap🧢",
        from_='+19377447658',
        to='+918446487230'
    )
    print(message.status)