#Applying a ReLU activation function on a set of output values

import numpy as np

lst_Output = [0.5, -3.7, 14.095, 10.5, -2.8, -15, 0, 0.135]
lst_Activated_Output = np.maximum(0,lst_Output)

print(lst_Activated_Output)