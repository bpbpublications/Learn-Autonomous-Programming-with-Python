#Calculate the sum of two matrices

import numpy as np

matrix_1 = np.random.rand(3,4)*10

matrix_2 = np.random.rand(3,4)*10

matrix_sum = matrix_1 + matrix_2

print('\nThis is a program to calculate the sum of two matrices having randomly generated values:\n')

print('\nThe first matrix is:\n')
print(matrix_1)

print('\nThe second matrix is:\n')
print(matrix_2)

print('\nThe matrix sum is:\n')
print(matrix_sum)