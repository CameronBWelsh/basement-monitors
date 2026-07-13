import adafruit_dht
import board
import time
import RPi.GPIO as GPIO

def read_dht22():
    sensor = adafruit_dht.DHT22(board.D17)
    while True:
        try:
            return round(sensor.temperature * 1.8 + 32, 1), sensor.humidity
        except RuntimeError as e:
            time.sleep(2)

def read_water():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN)
    if GPIO.input(27) == 0:
        return True
    if GPIO.input(27) == 1:
        return False

