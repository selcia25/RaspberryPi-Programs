import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setwarnings(False)

while True:
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    time.sleep(1)