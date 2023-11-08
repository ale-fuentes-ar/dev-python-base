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

while True:

    try:
        temp = float(input("Please, write temperature in graus: ").strip())
    except ValueError:
        log.error("ERROR: please write a correct temperature")
        continue
    
    try:
        humd = float(input("Please, write humidity: ").strip())
    except ValueError:
        log.error("ERROR: please write a correct temperature")
        continue
    
    
    print(f"now the weather is {temp} graus with {humd} humidity")

    if temp > 45:
        print("ALERT!!! danger to hot extreme")
    elif (temp * 3) >= humd:
        print("ALERT!!! danger to hot extreme with humidity")               
    elif temp in range(10, 31):
        print("Normal weather")
    elif temp in range(0, 10):
        print("Cold weather")
    elif temp < 0:
        print("ALERT!!! danger, cold extreme")

    if input("You want try more one [N, y]").strip().lower() != 'y':
        break

