#Implementing a neural network

import numpy as np

lst_inputs = [3,10,9.7]

arr_weights = [[0.5, 0.9, 0.35],
               [0.1, 0.3, 0.93],
               [0.91, 0.72, 0.1],
               [1.0, 0.31, 0.75]]

lst_bias = [0.2,0.95,1.0,4.0]

hidden_layer_output = np.dot(arr_weights, lst_inputs) + lst_bias

print(hidden_layer_output)








     