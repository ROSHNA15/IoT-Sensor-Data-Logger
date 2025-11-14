import csv
import random
import time
from datetime import datetime

# File to store sensor data
filename = "sensor_data.csv"

# Create CSV file and header if not present
header = ["Timestamp", "Temperature (°C)", "Humidity (%)", "Voltage (V)"]

try:
    with open(filename, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
except FileExistsError:
    pass  # File already exists, skip header creation

def generate_sensor_data():
    """Simulates random sensor readings."""
    temperature = round(random.uniform(20.0, 40.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    voltage = round(random.uniform(3.0, 5.0), 2)
    return temperature, humidity, voltage

print("IoT Sensor Data Logger Started...\nLogging data every 2 seconds.\nPress Ctrl+C to stop.\n")

try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature, humidity, voltage = generate_sensor_data()

        # Append data to CSV file
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, temperature, humidity, voltage])

        print(f"{timestamp} | Temp: {temperature}°C | Humidity: {humidity}% | Voltage: {voltage}V")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nData logging stopped by user.")
