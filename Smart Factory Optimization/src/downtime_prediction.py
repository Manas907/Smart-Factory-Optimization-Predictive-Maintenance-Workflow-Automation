import random

def predict_downtime(sensor_data):
    risk_factor = (sensor_data["temperature"] / 100) + (sensor_data["vibration"] / 5)
    return "High Risk" if risk_factor > 1.5 else "Low Risk"

if __name__ == "__main__":
    test_data = {"temperature": 70, "vibration": 3.5}
    print("Downtime Risk:", predict_downtime(test_data))