import csv
import numpy as np

""" import data """
output = [list(i) for i in [i[0] for i in csv.reader(open('Data.csv'))]]


def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


""" Part 1 """
Cols = [0] *len(output[0])


for k in range(len(Cols)):
    for i in range(len(output)):
        Cols[k] += int(output[i][k])  
        # print(int(list(output[i][0])[k]))

gamma = [0] *len(output[0])
epsilon = [0] *len(output[0])

for i in range(len(Cols)):
    if Cols[i] > len(output)/2:
        gamma[i] = 1
    else:
        epsilon[i] = 1

print(binatodeci(epsilon)*binatodeci(gamma))

""" Part 2 """
def sorter(values,i):
    tick=0
    new_values = []
    for j in range(len(values)):
        tick += int(values[j][i])
    
    if tick > len(values)/2:
        for j in range(len(values)):
            if values[j][i] == '1':
                new_values.append(values[j])

    elif tick < len(values)/2: 
        for j in range(len(values)):
            if values[j][i] == '0':
                new_values.append(values[j])

    else:  
        for j in range(len(values)):
            if values[j][i] == '1':
                new_values.append(values[j])
    return new_values
    
def sorter2(values,i):
    tick=0
    new_values = []
    for j in range(len(values)):
        tick += int(values[j][i])
    
    if tick > len(values)/2:
        for j in range(len(values)):
            if values[j][i] == '0':
                new_values.append(values[j])

    elif tick < len(values)/2: 
        for j in range(len(values)):
            if values[j][i] == '1':
                new_values.append(values[j])

    else:  
        for j in range(len(values)):
            if values[j][i] == '0':
                new_values.append(values[j])
    return new_values

oxygen = output


for i in range(len(oxygen[0])):
    oxygen_val = [0]*len(oxygen[0])
    oxygen = sorter(oxygen,i)
    if len(oxygen) == 1:
        print(oxygen)
        for j in range(len(oxygen[0])):
            oxygen_val[j] = int(oxygen[0][j]) 
        ox = (binatodeci(oxygen_val))
        break

co2 = output

for i in range(len(co2[0])):
    co2_val = [0]*len(co2[0])
    co2 = sorter2(co2,i)
    if len(co2) == 1:
        for j in range(len(co2[0])):
            co2_val[j] = int(co2[0][j]) 
        co = (binatodeci(co2_val))
        break

print(co*ox)