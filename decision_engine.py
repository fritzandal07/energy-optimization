import time
import csv
from datetime import datetime

SENSOR_LOG = "log/sensor_log.csv"
DECISION_LOG = "log/decisions.log"

# Read the entire sensor log file and return all rows except the header
def read_logs():
    with open(SENSOR_LOG, "r") as f:
        lines = f.readlines()
    return lines[1:]  # Skip the header

# Apply decision logic based on temperature and occupancy
def make_decision(temp, occupancy):
    temp = float(temp)  # Convert temperature to float
    occupancy = int(occupancy)  # Convert occupancy to int
    if occupancy == 1:  # Occupied room
        if temp < 20:
            return "raise setpoint"
        elif temp > 24:
            return "lower setpoint"
    else:  # Unoccupied room
        if temp > 24:
            return "lower setpoint"
    return "do nothing"

# Main loop to process sensor logs and make decisions
def main():
    processed_logs = set()  # To track which logs have been processed
    while True:
        logs = read_logs()  # Read all the logs
        for log in logs:
            temp, occ, power = log.strip().split(",")  # Parse the values from the log
            if log not in processed_logs:  # Ensure the log is not processed again
                decision = make_decision(temp, occ)  # Make a decision based on temp and occupancy

                # Write the decision to the decision log
                with open(DECISION_LOG, "a") as f:
                    f.write(f"{datetime.now().isoformat()} - Temp: {temp}, Occ: {occ} => {decision}\n")

                print(f"Decision logged: {decision}")  # Print the decision for confirmation
                processed_logs.add(log)  # Add log to processed set to avoid duplicate processing

        time.sleep(1)  # Wait before checking the log again

if __name__ == "__main__":
    main()
