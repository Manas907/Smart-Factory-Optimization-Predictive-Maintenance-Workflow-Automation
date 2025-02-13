import matplotlib.pyplot as plt

def plot_data(data):
    temperatures = [entry["temperature"] for entry in data]
    vibrations = [entry["vibration"] for entry in data]
    
    plt.figure()
    plt.plot(temperatures, label="Temperature")
    plt.plot(vibrations, label="Vibration")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    sample_data = [{"temperature": 60 + i, "vibration": 2 + i*0.1} for i in range(10)]
    plot_data(sample_data)