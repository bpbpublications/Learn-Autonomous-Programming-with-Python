#Implementing a neural network

lst_inputs = [3,10,9.7]

lst_weights_1 = [0.5, 0.9, 0.35]

lst_weights_2 = [0.1, 0.3, 0.93]

lst_weights_3 = [0.91, 0.72, 0.1]

lst_weights_4 = [1.0, 0.31, 0.75]

lst_bias = [0.2,0.95,1.0,4.0]



y1 = lst_inputs[0]*lst_weights_1[0]+\
     lst_inputs[1]*lst_weights_1[1]+\
     lst_inputs[2]*lst_weights_1[2] + lst_bias[0]
     
y2 = lst_inputs[0]*lst_weights_2[0]+\
     lst_inputs[1]*lst_weights_2[1]+\
     lst_inputs[2]*lst_weights_2[2] + lst_bias[1]
     
y3 = lst_inputs[0]*lst_weights_3[0]+\
     lst_inputs[1]*lst_weights_3[1]+\
     lst_inputs[2]*lst_weights_3[2] + lst_bias[2]
     
y4 = lst_inputs[0]*lst_weights_4[0]+\
     lst_inputs[1]*lst_weights_4[1]+\
     lst_inputs[2]*lst_weights_4[2] + lst_bias[3]
     

print('y1 = ' + str(y1))
print('y2 = ' + str(y2))
print('y3 = ' + str(y3))
print('y4 = ' + str(y4))
     