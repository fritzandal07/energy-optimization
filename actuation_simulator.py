import logging
import time

# Set up logging for actuator simulation
logging.basicConfig(filename='log/actuator.log', level=logging.INFO)

# Read the last line of the log file
def read_last_line(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:
                return None  # No data in the log file
            return lines[-1].strip()  # Get the last line
    except FileNotFoundError:
        return None  # Log file does not exist yet

def main():
    processed = set()  # Set to track already processed decisions
    while True:
        line = read_last_line('log/decisions.log')  # Read the last decision made
        if line and line not in processed:  # If there's a new decision and it hasn't been processed yet
            if "raise setpoint" in line or "lower setpoint" in line:  # Check if the action is to raise or lower setpoint
                action = f"{line} => Simulating actuator change"  # Simulate the actuator action
                logging.info(action)  # Log the actuator action
                print(action)  # Print the action to console
            else:
                print(f"{line} => No action required")  # Print if no action is needed
            processed.add(line)  # Add this line to the processed set
        time.sleep(1)  # Sleep for a while before checking the log again

if __name__ == "__main__":
    main()
