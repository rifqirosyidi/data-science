import numpy as np

data = np.loadtxt("load_data_exp.txt", skiprows=1, dtype=np.uint8, delimiter=',')

print(data)
print(data.dtype)