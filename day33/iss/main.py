import requests
import datetime
import smtplib
import time

MY_LAT = 32.715736 # Your latitude
MY_LONG = -117.161087 # Your longitude

my_email = "jackw1689@gmail.com"

password = "eldxlwscmsvxewuv"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
lat_range = [(iss_latitude-5).__floor__(),(iss_latitude+5).__floor__()]
lng_range = [(iss_longitude-5).__floor__(),(iss_longitude+5).__floor__()]
lat_min = lat_range[0]
lat_max = lat_range[1]
lng_min = lng_range[0]
lng_max = lng_range[1]


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data = response.json()['results']
sunrise=datetime.datetime.fromisoformat(data['sunrise'])
sunset=datetime.datetime.fromisoformat(data['sunset'])

localsunrise = sunrise.astimezone(tz=None)
localsunset = sunset.astimezone(tz=None)

time_now = datetime.datetime.now()



def is_dark():
    print(time_now.hour)
    print(localsunset.hour)
    return True if localsunset.hour+1>localsunset.hour else False

def check_ISS_range():
    print(f'{lat_min}, {MY_LAT}, {lat_max}')
    print(f'{lng_min}, {MY_LONG}, {lng_max}')

    if MY_LAT>lat_min and MY_LAT<lat_max and MY_LONG>lng_min and MY_LONG<lng_max:
        return True
    return False

def runapp():
    while True:
        time.sleep(60)
        if is_dark() and check_ISS_range():
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(from_addr=my_email, to_addrs='jackw1689@gmail.com',msg='Subject:ISS station overhead\n\n look up!')

        else:
            print('ISS NOT OVERHEAD')

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
runapp()


