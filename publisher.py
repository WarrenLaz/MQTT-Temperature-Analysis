# Import package
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import time
import datetime
import json
import time
import board
import adafruit_dht


# Load environment variables from .env file
load_dotenv()
print(os.getenv('MQTT_HOST'))
class _Publisher_:
    def __init__(self):
        # Initiate MQTT Client
        self.mqttc = mqtt.Client()
        
        try:
            # Define Variables from environment variables
            self.MQTT_HOST = os.getenv('MQTT_HOST')
            self.MQTT_PORT = int(os.getenv('MQTT_PORT'))
            self.MQTT_KEEPALIVE_INTERVAL = int(os.getenv('MQTT_KEEPALIVE_INTERVAL'))
            self.MQTT_TOPIC = os.getenv('MQTT_TOPIC')
            self.sensor = adafruit_dht.DHT22(board.D4)
        except Exception as e:
            print(f"Error loading environment variables: {e}")

    # Define on_connect event handler
    def on_connect(self, mosq, obj, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.mqttc.subscribe(self.MQTT_TOPIC, qos=0)
        else:
            print(f"Connection failed with error code {rc}")

    # Define on_publish event handler
    def on_publish(self, client, userdata, mid):
        print("Message Published...")

    def run(self):
        # Register event handlers
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish

        try:
            # Connect to MQTT Broker
            self.mqttc.connect(self.MQTT_HOST, self.MQTT_PORT, self.MQTT_KEEPALIVE_INTERVAL)
            print(f"Connecting to {self.MQTT_HOST}:{self.MQTT_PORT}")

            self.mqttc.loop_start()
            # Publish a message to the MQTT Topic
            while True:
                try:
                # Print the values to the serial port
                    temperature_c = self.sensor.temperature
                    temperature_f = temperature_c * (9 / 5) + 32
                    humidity = self.sensor.humidity
                    print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
                except RuntimeError as error:
                    # Errors happen fairly often, DHT's are hard to read, just keep going
                    print(error.args[0])
                except Exception as error:
                    self.sensor.exit()
                    raise error
                
                self.mqttc.publish(self.MQTT_TOPIC, json.dumps(
                    {"Time" : datetime.datetime.now().isoformat(),
                     "temperature_c" : temperature_c,
                     "temperature_f" : temperature_f,
                     "humidty" : humidity
                     }))
                time.sleep(10)

        except Exception as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    pub = _Publisher_()
    pub.run()
