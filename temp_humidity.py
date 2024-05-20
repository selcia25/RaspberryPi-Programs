# python3 -m pip install adafruit-circuitpython-dht
import Adafruit_DHT
import time

# Set the type of sensor and the GPIO pin to which it is connected
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Replace with the GPIO pin number you are using

while True:
    # Read humidity and temperature
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
    else:
        print("Failed to retrieve data from the sensor")
    
    # Wait for 2 seconds before reading again
    time.sleep(2)
