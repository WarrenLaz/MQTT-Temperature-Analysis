# Import package
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
load_dotenv()

class _Subscriber_:
    def __init__(self):
        # Initiate MQTT Client
        self.mqttc = mqtt.Client()
        
        try:
            # Define Variables
            self.MQTT_HOST = os.getenv('MQTT_HOST')
            self.MQTT_PORT = int(os.getenv('MQTT_PORT'))
            self.MQTT_KEEPALIVE_INTERVAL = int(os.getenv('MQTT_KEEPALIVE_INTERVAL'))
            self.MQTT_TOPIC = os.getenv('MQTT_TOPIC')
        except Exception as e:
            print(f"Error loading MQTT environment variables: {e}")

    def on_connect(self, mosq, obj, flags, rc):
        """Handle MQTT connection event."""
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.mqttc.subscribe(self.MQTT_TOPIC, qos=0)
        else:
            print(f"Connection failed with error code {rc}")

    def on_subscribe(self, mosq, obj, mid, granted_qos):
        """Handle subscription event."""
        print("Subscribed to MQTT Topic")

    def on_message(self, mosq, obj, msg):
        """Handle incoming messages."""
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

    def run(self):
        """Start MQTT Client."""
        # Register Event Handlers
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.on_subscribe = self.on_subscribe

        # Connect with MQTT Broker
        try:
            self.mqttc.connect(self.MQTT_HOST, self.MQTT_PORT, self.MQTT_KEEPALIVE_INTERVAL)
            print(f"Connecting to {self.MQTT_HOST}:{self.MQTT_PORT}")
            self.mqttc.loop_forever()
        except Exception as e:
            print(f"Connection failed: {e}")

if __name__ == '__main__':
    sub = _Subscriber_()
    sub.run()
