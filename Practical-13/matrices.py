import numpy as ny

m1 = ny.array([[1, 2, 3], [4, 5, 6]])
m2 = ny.array([[7, 8, 9], [10, 11, 10]])
print("Matrix 1 : {0} \nMatrix 2 : {1} ".format(m1, m2))
print("Addition Of Matrix : ",ny.add(m1,m2))
print("Subtraction Of Matrix : ",ny.subtract(m1,m2))
print("Multiplication Of Matrix : ",ny.multiply(m1,m2))
print("Division Of Matrix : ",ny.divide(m1,m2))


