import csv

""" import data """
output = [ i[0].split(' ') for i in csv.reader(open('Data.csv'))]

""" part 1 """

h = 0
d = 0

for i in range(len(output)):
    if output[i][0] == 'forward':
        h += int(output[i][1])

    elif output[i][0] == 'down':
        d += int(output[i][1])

    elif output[i][0] == 'up':
        d -= int(output[i][1])

print(f'd = {d}, h = {h}, answer 1 = {d*h}')

""" part 2 """
h = 0
d = 0
aim = 0

for i in range(len(output)):
    if output[i][0] == 'forward':
        h += int(output[i][1])
        d += aim * int(output[i][1])

    elif output[i][0] == 'down':
        aim += int(output[i][1])

    elif output[i][0] == 'up':
        aim -= int(output[i][1])

print(f'd = {d} h = {h} answer 2 = {d*h}')
