import sensor
import database
import time

counter = 0
while True: 
    if sensor.read_water():
        print("Water detected!")

    counter += 1
    if counter >= 60:
        temperature, humidity = sensor.read_dht22() 
        database.insert_reading(temperature, humidity) 
        counter = 0
   
    time.sleep(10)
