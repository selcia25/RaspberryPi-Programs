import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
while True:
    try:
        print(not GPIO.input(8))
        GPIO.output(36, GPIO.input(8))
        GPIO.output(32, GPIO.input(8))
    except KeyboardInterrupt:
        GPIO.cleanup()