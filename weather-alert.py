#!/usr/bin/env python3
"""alert of weather

This script show next alert:
* temp. greater than 45: "ALERT!!! danger to hot extreme"
* temp. * 3 was more than greater or equal to HUMIDITY: "ALERT!!! danger of hot and humidity"
* temp. between 10 and 30: "Normal weather"
* temp. between 0 and 10: "Cold weather"
* temp. less than 0: "ALERT!!! danger, cold extreme"
"""

import logging

log = logging.Logger("alert")
# TODO: use functions to read input
weather = {
    "temperature": None,
    "humidity": None
} # Dict / mutavel
keys = weather.keys()

while True:

    if all(weather.values()): # [None, None]
        break

    for key in keys:
        try:
            weather[key] = float(input(f"Please, write {key} in graus: ").strip())
        except ValueError:
            log.error("ERROR: for {key.capitalize}, please write a correct value")
            continue   
    
    print(f"now the weather is {weather['temperature']} graus with {weather['humidity']} humidity")

    temp = weather["temperature"]
    humi = weather["humidity"]

    if temp > 45:
        print("ALERT!!! danger to hot extreme")
    elif (temp * 3) >= humi:
        print("ALERT!!! danger to hot extreme with humidity")               
    # elif temp in range(10, 31): is better not use range because Python crate a new var in memory
    elif temp > 10 and temp <= 30:
        print("Normal weather")
    elif temp > 0 and temp <= 10:
        print("Cold weather")
    elif temp <= 0:
        print("ALERT!!! danger, cold extreme")

    if input("You want try more one [N, y]").strip().lower() != 'y':
        break

