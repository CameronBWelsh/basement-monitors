import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)

water = False
if GPIO.input(27) == 0:
    water = True
if water: 
    print("Water detected")
else:
    print("Dry")
