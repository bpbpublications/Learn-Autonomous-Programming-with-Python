#Backpropagation
import numpy as np
import matplotlib.pyplot as plt

def ReLU(z):
    return np.maximum(0,z)

def Sum(lst_inputs,arr_weights,lst_bias):
    return np.dot(arr_weights, lst_inputs) + lst_bias

def Error(output_E,output):
    return (1/2)*(output_E-output) ** 2

def dError(output_E,output):
    return output_E-output

def dRELU(z):
    return 1. if z > 0 else 0.

def dSum_w1(lst_inputs,arr_weights):
    return lst_inputs[0]    
    
lst_inputs = [3,10,9.7,0.95]

arr_weights = [0.5, 0.3, 0.93, 1.0]
              
lst_bias = [0.2]

output_E = 15.00

learning_rate = 0.01

output = ReLU(Sum(lst_inputs,arr_weights,lst_bias))[0]

Error_Value = Error(output_E,output)

dError_value = dError(output_E,output)

dRELU_value = dRELU(Sum(lst_inputs,arr_weights,lst_bias))

dSum_w1_value = dSum_w1(lst_inputs,arr_weights)

dError_w1 = dError_value*dRELU_value*dSum_w1_value

w1 = arr_weights[0]

w1_new = w1 - learning_rate*dError_w1

print(w1_new)
    
