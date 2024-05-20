import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

GPIO.output(8, GPIO.LOW)
time.sleep(2)
GPIO.output(8, GPIO.HIGH)
time.sleep(2)
GPIO.output(8, GPIO.LOW)
try:
    while GPIO.input(12) == 0:
        start = time.time()
    while GPIO.input(12) == 1:
        bounce = time.time()

    duration = bounce - start
    distance = round(duration * 17150, 2)
    print(f"Distance: {distance} cm")
except KeyboardInterrupt:
    GPIO.cleanup()