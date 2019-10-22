import requests
from twilio.rest import Client


def get_weather():
    weather_key = "84e47e1e1cca691ef6e53d7126dc1764"
    url = "http://api.openweathermap.org/data/2.5/weather?id="
    params = {"APPID": weather_key, "q": "Chicago", "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()
    temp = format_response(weather)[0]
    desc = format_response(weather)[1]
    text_message(temp, desc)


def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = str(int(weather["main"]["temp"]))
        result = [temp, desc]
    except:
        result = ["Cannot retrieve that information", ""]

    return result


def text_message(temp, desc):
    account_sid = "ACc11052ae22166bc9ba018eac3eb968de"
    auth_token = "549dbd93cfc861ae3ec1273b22c205df"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is currently {} degrees with {}".format(temp, desc),
        from_="+18727135673",
        to="+17734561045",
    )
    print(message.sid)


get_weather()
