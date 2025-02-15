
"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-temperature-sensor
"""


from w1thermsensor import W1ThermSensor
import time

# Find the connected DS18B20 sensor
def find_ds18b20_sensor():
    for sensor in W1ThermSensor.get_available_sensors():
        if sensor.type == W1ThermSensor.THERM_SENSOR_DS18B20:
            return sensor
    return None

# Read temperature from the sensor
def read_temperature(sensor):
    temperature_celsius = sensor.get_temperature()
    temperature_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
    return temperature_celsius, temperature_fahrenheit

# Find DS18B20 sensor
ds18b20_sensor = find_ds18b20_sensor()

if ds18b20_sensor is not None:
    print(f"DS18B20 Sensor found: {ds18b20_sensor.id}")

    try:
        while True:
            # Read temperature
            temperature_c, temperature_f = read_temperature(ds18b20_sensor)
            
            print(f"Temperature: {temperature_c:.2f}°C | {temperature_f:.2f}°F")
            
            # Wait for a moment before reading again
            time.sleep(2)

    except KeyboardInterrupt:
        print("Program terminated by user.")

else:
    print("DS18B20 Sensor not found.")