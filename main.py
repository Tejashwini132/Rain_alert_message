import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "f108aea31ce719fb049d3d151b500fa7"
account_sid = "AC9b1c5eb4acd340b0bb26684e7b65b92f"
auth_token = "a0b3c5bc872547359e7dd35fdd801fc7"

parameters = {"lat": 12.976750,
              "lon": 77.575279,
              "appid": api_key,
              "exclude": "current,minutely,daily"}
response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today.Remember to get a Umbrella",
        from_="+19282720977",
        to="+917022120036"
    )
    print(message.status)