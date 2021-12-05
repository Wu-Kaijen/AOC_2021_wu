""" import data """
from typing import Set


sets = [i.strip() for i in open('Data.txt').readlines()]
Sets = [sets[x+1:x+6] for x in range(0,len(sets),6)]
numbers = [i for i in open('Data_input.txt').readlines()[0].strip().split(',')]

""" Part 1 """
def checkrows(row,set):
    if all(elem in set for elem in row):
        return True
    else:
        return False


def checkcolumns(column,set):
    if all(elem in set for elem in column):
        return True
    else:
        return False

def solver(numbers,Sets):
    for i in range(len(numbers)):
        for j in range(len(Sets)):
            for k in range(len(Sets[0])):
                column = []
                for l in range(len(Sets[0])):
                    column.append(Sets[j][l].split()[k])

                if checkcolumns(column,numbers[0:i+1]):
                    final =0
                    for r in range(len(Sets[0])):
                        for c in range(len(Sets[0])):
                            if Sets[j][r].split()[c] not in numbers[0:i+1]:
                                final += int(Sets[j][r].split()[c])
                    return print(f'last number = {numbers[i]}, sum = {final}, solution1 = {int(numbers[i])  * final  }')
                if checkrows(Sets[j][k].split(),numbers[0:i+1]):
                    final =0
                    for r in range(len(Sets[0])):
                        for c in range(len(Sets[0])):
                            if Sets[j][r].split()[c] not in numbers[0:i+1]:
                                final += int(Sets[j][r].split()[c])
                    return print(f'last number = {numbers[i]}, sum = {final}, solution1 = {int(numbers[i])  * final  }')
            
solver(numbers,Sets)

""" Part 2 """

def solversingle(numbers,Sets,set):
    for i in range(len(numbers)):
        for k in range(len(Sets[0])):
            column = []
            for l in range(len(Sets[0])):
                column.append(Sets[set][l].split()[k])

            if checkcolumns(column,numbers[0:i+1]) or checkrows(Sets[set][k].split(),numbers[0:i+1]):
                return i


def part2(Sets,numbers):
    num = []
    for i in range(len(Sets)):
        num.append(solversingle(numbers,Sets,i))
    max_num = max(num)
    max_idx = num.index(max_num)
    final =0
    for r in range(len(Sets[0])):
        for c in range(len(Sets[0])):
            if Sets[max_idx][r].split()[c] not in numbers[0:num[max_idx]+1]:
                final += int(Sets[max_idx][r].split()[c])
    return print(f'last number = {numbers[max_num]}, sum = {final}, solution2 = {int(numbers[max_num])  * final  }')
        
part2(Sets,numbers)
print(f'answer2 = {1}')



