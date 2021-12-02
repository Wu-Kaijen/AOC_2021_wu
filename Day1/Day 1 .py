import numpy as np
import csv

""" input data  """
output = [ int(i[0]) for i in csv.reader(open('Data_test.csv'))]

""" part 1 """
n = 0 
for i in range(1,len(output)):
    if output[i] > output[i-1]:
        n += 1

""" part 2 """
N = 0
for i in range(0,len(output)-3):
    if output[i+3] > output[i]:
        N += 1

""" output """
print(f'number of increases {n}')
print(f'number of sliding increases {N}')
