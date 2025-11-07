from collections import deque
import matplotlib.pyplot as plt
import time
from src.config import VEHICLE_CLASSES, MAX_HISTORY, PLOT_COLOR

class DensityAnalyzer:
 
    def __init__(self):
        self.density_history = deque(maxlen=MAX_HISTORY)
        self.timestamps = deque(maxlen=MAX_HISTORY)
        self.start_time = time.time()

    def count_vehicles(self, results, model):
     
        count = 0
        if results and results[0].boxes.id is not None:
            for cls_tensor in results[0].boxes.cls:
                cls_name = model.names[int(cls_tensor)]
                if cls_name in VEHICLE_CLASSES:
                    count += 1
        return count

    def update(self, count):
  
        self.density_history.append(count)
        self.timestamps.append(time.time() - self.start_time)

    def plot_density(self):
      
        plt.figure(figsize=(10, 5))
        plt.plot(self.timestamps, self.density_history, label="Vehicle Density", color=PLOT_COLOR)
        plt.xlabel("Time (s)")
        plt.ylabel("Vehicle Count")
        plt.title("Real-Time Vehicle Density Analysis")
        plt.legend()
        plt.tight_layout()
        plt.show()
