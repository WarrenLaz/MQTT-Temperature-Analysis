import pandas as pd
import matplotlib.pyplot as plt
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB connection setup
URI = os.getenv('MONGO_URI')
CLIENT = MongoClient(URI, server_api=ServerApi('1'))
COLLECTION = CLIENT[os.getenv('DB_NAME')][os.getenv('COLLECTION_NAME')]

# Fetch data from MongoDB
entries = COLLECTION.find({})

# Convert MongoDB cursor to a list of dictionaries
entries_list = list(entries)

# Create a DataFrame from the entries
df = pd.DataFrame(entries_list)

# Convert 'Time' column to datetime and set it as the index
df['Time'] = pd.to_datetime(df['Time'])
df.set_index('Time', inplace=True)

# Plotting the data in three separate subplots
plt.figure(figsize=(10, 10))

# Plotting Celsius temperature
plt.subplot(3, 1, 1)
plt.plot(df.index, df['temperature_c'], label='Temperature (°C)', color='red')
plt.title('Temperature (°C) over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()

# Plotting Fahrenheit temperature
plt.subplot(3, 1, 2)
plt.plot(df.index, df['temperature_f'], label='Temperature (°F)', color='blue')
plt.title('Temperature (°F) over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°F)')
plt.legend()

# Plotting humidity
plt.subplot(3, 1, 3)
plt.plot(df.index, df['humidity'], label='Humidity (%)', color='green')
plt.title('Humidity over Time')
plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
