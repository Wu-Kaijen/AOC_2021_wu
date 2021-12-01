import numpy as np
import csv

with open('Data.csv', newline= '') as file: 
    reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC, delimiter =  ' ')
    output  = []
    for row in reader:
        output.append(row[:])


n = 0 
for i in range(1,len(output)):
    if output[i][0] > output[i-1][0]:
        n += 1


N = 0
for i in range(0,len(output)-2):
    if output[i+3][0] > output[i][0]:
        N += 1