import numpy as np

def optimize_workflow(sensor_data):
    """ Basic heuristic for suggesting workflow improvements """
    avg_efficiency = np.mean(sensor_data['efficiency'])
    if avg_efficiency < 75:
        return "Increase machine maintenance intervals and optimize workflow."
    return "Workflow efficiency is optimal."

# Example usage
sensor_data = {'efficiency': [78, 72, 80, 65]}
print(optimize_workflow(sensor_data))