import adafruit_dht
import board
import time

sensor = adafruit_dht.DHT22(board.D17)

while True:
    try:
        print((sensor.temperature * 1.8) + 32)
        print(sensor.humidity)
        break
    except RuntimeError as e:
        print("Reading failed, retrying...")
        time.sleep(2)
