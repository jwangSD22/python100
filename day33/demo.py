import requests
import datetime

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# data = response.json()['iss_position']
# lat = data['latitude']
# lng = data['longitude']

# print((lat,lng))

lat = 32.715736
lng =  -117.161087


parameters = {
    'lat':lat,
    'lng':lng,
    'formatted':0
}

response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
data = response.json()['results']
sunrise=datetime.datetime.fromisoformat(data['sunrise'])
sunset=datetime.datetime.fromisoformat(data['sunset'])

print(sunrise,sunset)

localsunrise = sunrise.astimezone(tz=None)
localsunset = sunset.astimezone(tz=None)

sr = localsunrise.strftime('%I:%M %p')
ss = localsunset.strftime('%I:%M %p')


print((sr,ss))