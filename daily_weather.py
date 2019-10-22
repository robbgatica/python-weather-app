import requests
from twilio.rest import Client


def get_weather():
    weather_key = "Enter Your API Key Here"
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
    account_sid = "Enter Your Twilio SID Here"
    auth_token = "Enter Your Token Here"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is currently {} degrees with {}".format(temp, desc),
        from_="+Enter Your Twilio Number Here",
        to="+Enter the Destination Phone Number Here",
    )
    print(message.sid)


get_weather()
