import time
import numpy as np

# Setting memory for cpu
physical_memory = 8 * 1024 * 1024 * 1024 # 8GB
active_memory_set = 6 * 1024 * 1024 * 1024 # 6GB
page_size = 4 * 1024 # 4KB
M = active_memory_set // page_size

C_values = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1.0, 1.01, 1.1, 1.5, 2, 5, 10, 50])
C_values = (C_values * M).astype(int)

# Number of operations used
num_ops = 10000

# Create a random dataset
dataset = np.random.rand(1000, 1000)

# Perform computations for different values of C
timings = []
for C in C_values:
    
    start_time = time.time()
    data = dataset[:C, :C]
    
    result = data
    # Matrix multiplication of result and data
    for i in range(num_ops - 1):
        result = np.dot(result, data)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    timings.append(elapsed_time)

import matplotlib.pyplot as plt
plt.plot(C_values, timings)
plt.xlabel("Dataset size (pages)")
plt.ylabel("Execution time (seconds)")
plt.show()