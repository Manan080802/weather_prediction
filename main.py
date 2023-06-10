import  requests
from twilio.rest import Client

account_sid = "account sid"
auth_token="auth token"
OWN_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast?lat=23.022505&lon=72.571365&appid=id"
response = requests.get(OWN_ENDPOINT)
response.raise_for_status()
data = response.json()
weather_slice = data["list"][:12]
# print(weather_slice)
will_rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    # if int(condition_code) < 700:
    #     # print("Being an umbrella")
    #     client = Client(account_sid, auth_token)
    #     message = client.messages.create(
    #         body="It's going to sun today, Remember to today is heatwaves",
    #         from_="+13613152496",
    #         to="+91 91044 99002"
    #     )
    #     print(message.status)
    #     will_rain = True
    if int(condition_code)>=800:
        # print("Heat waves")
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     body="It's going to sun today, Remember to today is heatwaves",
        #     from_="+13613152496",
        #     to="+91 91044 99002"
        # )
        # print(message.status)
        will_rain=True
if will_rain:
    client = Client(account_sid,auth_token)
    message =client.messages.create(
        body="It's going to sun today, Remember to today is heatwaves",
        from_="+ twilio number",
        to="+91 your number"
    )
    print(message.status)
    # print("Heat waves")
# print(data["list"][0]["weather"][0])
# https://api.openweathermap.org/data/2.5/weather?q=Ahmedabad&appid=f900bf1c8e8f4f2e5927c5049cef6efd