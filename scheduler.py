import sensor
import database
import time
import requests

counter = 0
alert_counter = 0
while True: 
    if sensor.read_water() and alert_counter < 3:
        requests.post("https://ntfy.sh/welsh-basement-alarm-631621", data="Water detected in basement!")
        alert_counter += 1
    elif not sensor.read_water() and alert_counter > 0:
        alert_counter = 0

    counter += 1
    if counter >= 60:
        try:
            temperature, humidity = sensor.read_dht22() 
            database.insert_reading(temperature, humidity) 
        except Exception as e:
            print(f"Sensor error: {e}")
        counter = 0
   
    time.sleep(10)
