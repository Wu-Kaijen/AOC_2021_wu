""" load Data """
data = [int(j) for j in [i.split(',') for i in open('Data.txt').readlines() ][0]]
""" part 1 """

feul = []
for j in range(0,max(data)+1):
    feul.append( sum([abs(i-j) for i in data]))

print(min(feul))

""" part 2 """

feul = []
for j in range(0,max(data)+1):
    feul.append( sum([ abs(i-j) *(abs(i-j) +1) /2 for i in data]))

print(int(min(feul)))
