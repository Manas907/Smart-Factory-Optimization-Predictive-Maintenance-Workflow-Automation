import random
import time

def get_live_sensor_data():
    """ Simulates fetching live sensor data """
    return {
        'temperature': random.uniform(30, 80),
        'vibration': random.uniform(0.1, 1.5),
        'efficiency': random.uniform(60, 95)
    }

while True:
    data = get_live_sensor_data()
    print("Live Data:", data)
    time.sleep(2) 