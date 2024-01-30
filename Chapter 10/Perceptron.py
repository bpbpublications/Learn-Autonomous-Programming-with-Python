# Implementation of a perceptron

lst_inputs = [5,3.7,1.3,2.75]

lst_weights = [0.8,0.5,-0.3,1.0]

dbl_bias = 3.5

dbl_output = (lst_inputs[0]*lst_weights[0] \
             + lst_inputs[1]*lst_weights[1] \
            + lst_inputs[2]*lst_weights[2]+ \
            lst_inputs[3]*lst_weights[3]) + dbl_bias

print(dbl_output)
