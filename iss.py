import yagmail
import requests
import datetime as dt
import os
import time


def iss_checker():
    #Mannheim
    MY_LAT = '49.497450'
    MY_LNG = '8.457550'
    #------------------------CODE-------------------------#
    times = 0

    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    latiitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    iss_position = (float(latiitude), float(longitude))
    #print(f"The current ISS location is : {iss_position}")

    with open('iss_data.csv', 'a+') as file:
            file.write(f'{iss_position},{dt.datetime.now()}\n')
    
    parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
    my_location = (MY_LAT, MY_LNG)
    #print(f"My current location is: {my_location}")
    if iss_position[0] <= float(MY_LAT) + 5 and iss_position[0] >= float(
            MY_LAT) - 5 and iss_position[1] <= float(
                MY_LNG) + 5 and iss_position[1] >= float(MY_LNG) - 5:

        url = "https://api.sunrise-sunset.org/json"
        response = requests.get(url, params=parameters)
        response.raise_for_status()

        data = response.json()
        sunrise = data["results"]["sunrise"]
        sunset = data["results"]["sunset"]

        sunrise_splitted_data = sunrise.split("T")[1].split(":")
        sunset_splitted_data = sunset.split("T")[1].split(":")

        sunrise_hour = int(sunrise_splitted_data[0]) + 1
        sunrise_minute = sunrise_splitted_data[1]

        sunset_hour = int(sunset_splitted_data[0]) + 1
        sunset_minute = sunset_splitted_data[1]

        now = dt.datetime.now().hour

        if now >= sunset_hour or now <= sunrise_hour:
            sender = yagmail.SMTP(user='MAIL',
                                  password='PASSWORD')
            sender.send(to='MAIL',
                        subject="The ISS is over your head",
                        contents="You have to look up right now!")
            print("Look up")
        else:
            print(
                "The ISS is over your head but the sky is to light to see it.")
        times += 1
        print(f"The code ran {times} times.")
        time.sleep(60)
    else:
        time.sleep(60)    
