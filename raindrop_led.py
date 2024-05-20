import RPi.GPIO as GPIO
import time

# GPIO pins for raindrop sensor and LEDs
sensor_pin = 17
led_pin_1 = 23
led_pin_2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(led_pin_2, GPIO.OUT)

try:
    while True:
        if GPIO.input(sensor_pin):
            # No water detected
            GPIO.output(led_pin_1, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.LOW)
            print("No water detected")
        else:
            # Water detected
            GPIO.output(led_pin_1, GPIO.HIGH)
            GPIO.output(led_pin_2, GPIO.HIGH)
            print("Water detected")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
