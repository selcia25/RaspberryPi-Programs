import RPi.GPIO as GPIO
import time

# Define physical pin numbers for the LEDs
red_pin = 11
yellow_pin = 13
green_pin = 15

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

# Function to turn off all LEDs
def all_off():
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)

try:
    while True:
        # Red light
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
        time.sleep(2)

        # Yellow light
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.LOW)
        time.sleep(1)

        # Green light
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
        time.sleep(2)

finally:
    # Clean up GPIO
    all_off()
    GPIO.cleanup()
