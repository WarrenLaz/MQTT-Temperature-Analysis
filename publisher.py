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
def on_connect(mosq, obj, rc):
	print ("Connected to MQTT Broker")

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print ("Message Published...")

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

# Publish message to MQTT Topic 
mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()