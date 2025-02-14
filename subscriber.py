# Import package
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
load_dotenv()

try:
    # Define Variables
    MQTT_HOST = os.getenv('MQTT_HOST')
    MQTT_PORT = int(os.getenv('MQTT_PORT'))
    MQTT_KEEPALIVE_INTERVAL = int(os.getenv('MQTT_KEEPALIVE_INTERVAL'))
    MQTT_TOPIC = os.getenv('MQTT_TOPIC')
    MQTT_MSG = os.getenv('MQTT_MSG')
except Exception:
    print(Exception)

# Define on_connect event Handler
def on_connect(mosq, obj, flags, rc):
	#Subscribe to a the Topic
	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print ("Subscribed to MQTT Topic")

# Define on_message event Handler
def on_message(mosq, obj, msg):
	print (msg.payload.decode())

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL )

# Continue the network loop
mqttc.loop_forever()