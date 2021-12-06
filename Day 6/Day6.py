""" load Data """
data = [int(j) for j in [i.split(',') for i in open('Data.txt').readlines() ][0]]
""" part 1 """

age = {i:0 for i in range(9)}
for value in data:
        age[value] += 1

for day in range(0,80):
    age_next = {j:0 for j in range(9)}

    for i in range(9):
        if i == 8:
            age_next[8] += age[0]
            age_next[6] += age[0]
        else:
            age_next[i]  += age[i+1]
    age = age_next
print(f'N_fish after day {day+1} = {sum(age.values())}, \n ages =  {age}')

""" part 2 """

age = {i:0 for i in range(9)}
for value in data:
        age[value] += 1

for day in range(0,256):
    age_next = {j:0 for j in range(9)}

    for i in range(9):
        if i == 8:
            age_next[8] += age[0]
            age_next[6] += age[0]
        else:
            age_next[i]  += age[i+1]
    age = age_next
print(f'N_fish after day {day+1} = {sum(age.values())}, \n ages =  {age}')
