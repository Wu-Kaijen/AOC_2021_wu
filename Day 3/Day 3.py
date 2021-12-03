import csv
import numpy as np

""" import data """
output = [list(i) for i in [i[0] for i in csv.reader(open('Data.csv'))]]


def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

Cols = [0] *len(output[0])


for k in range(len(Cols)):
    for i in range(len(output)):
        Cols[k] += int(output[i][k])  
        # print(int(list(output[i][0])[k]))
print(output)

gamma = [0] *len(output[0])
epsilon = [0] *len(output[0])

for i in range(len(Cols)):
    if Cols[i] > len(output)/2:
        gamma[i] = 1
    else:
        epsilon[i] = 1

print(binatodeci(epsilon)*binatodeci(gamma))
