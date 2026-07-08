import sensor
import database
import time

while True: 
    temperature, humidity = sensor.read_dht22() 
    database.insert_reading(temperature, humidity) 
    time.sleep(600)
