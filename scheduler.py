import sensor
import database
import time
import requests

counter = 0
while True: 
    if sensor.read_water():
        requests.post("https://ntfy.sh/welsh-basement-alarm-631621", data="Water detected in basement!")

    counter += 1
    if counter >= 60:
        temperature, humidity = sensor.read_dht22() 
        database.insert_reading(temperature, humidity) 
        counter = 0
   
    time.sleep(10)
