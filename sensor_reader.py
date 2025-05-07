import csv
import time
import os
from pathlib import Path

log_path = 'log/sensor_log.csv'

# Make sure the log directory exists
Path("./log").mkdir(exist_ok=True, parents=True)


# Ensure header is written if file is empty
if not os.path.exists(log_path) or os.path.getsize(log_path) == 0:
    with open(log_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'occupancy', 'power'])

# Open the mock data CSV
with open('mock_data/sensor_data.csv') as sensor_file:
    sensor_reader = csv.reader(sensor_file)
    next(sensor_reader)  # Skip header

    for row in sensor_reader:
        temp, occ, power = row

        # Append sensor data to the log
        with open(log_path, 'a', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow([temp, occ, power])

        print(f"Temp: {temp}, Occ: {occ}, Power: {power}")
        time.sleep(5)
