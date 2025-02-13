import json
import time

def process_data(data):
    if data["machine_status"] == "fault":
        print("ALERT: Machine fault detected!")
    
    with open("sensor_log.json", "a") as f:
        f.write(json.dumps(data) + "\n")

if __name__ == "__main__":
    sample_data = {"temperature": 75, "vibration": 2.5, "machine_status": "fault"}
    process_data(sample_data)
