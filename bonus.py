# Chris Moody - Module 3 - Bonus - Bonus File

import statistics
import random

data = []

for nextDataPoint in range(1000): 
    data.append(random.randrange(1,10))

print("\n\n")
print("Data: ", data, "\n")
print("Variance: ", statistics.pvariance(data))
print("Std Dev: ", statistics.pstdev(data))
print("\n\n")