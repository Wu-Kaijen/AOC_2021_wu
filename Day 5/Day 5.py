""" import data """
Data = [ i.strip().replace(',',' -> ').split(' -> ') for i in open('Data.txt').readlines()]
for i in range(len(Data)):
    for j in range(len(Data[0])):
        Data[i][j] = int(Data[i][j])

""" Part 1"""
def parallel(line):
    if line[0] == line[2] or line[1] == line[3]:
        if line[1] > line[3]:
            line = [line[0],line[3],line[2],line[1]]
        if line[0] > line[2]:
            line = [line[2],line[1],line[0],line[3]]
        return line
    else:
        return []

def sorter(Data):
    Data_new = [parallel(i) for i in Data if parallel(i)]
    return Data_new

def part1(Data):
    lines = sorter(Data)
    x_max = 0
    y_max = 0
    for i in range(len(lines)):
        for j in [0,1]:
            if x_max < lines[i][j]:
                x_max = lines[i][j]
            if y_max < lines[i][j+1]:
                y_max = lines[i][j+1]

    grid = [ [0]*(x_max+1) for i in range(y_max+1)]

    for i in range(len(lines)):
        line =  lines[i]
        for x in range(line[0],line[2]+1):
            for y in range(line[1],line[3]+1):
                grid[y][x] += 1
 
    tick = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] > 1:
                tick+=1
    print(f'answer1 = {tick}')
    return grid
grid = part1(Data)

""" Part 2 """

def slope(line):
        if line[0] > line[2]:
            line = [line[2],line[3],line[0],line[1]]
        if line[1] > line[3]:
            return [line[0],line[1],line[2],line[3],-1]
        elif line[1] == line[3]:
            return [line[0],line[1],line[2],line[3],0]
        else:
            return [line[0],line[1],line[2],line[3],1]

def part1(Data):
    lines = [slope(i) for i in Data]
    x_max = 0
    y_max = 0
    for i in range(len(lines)):
        for j in [0,1]:
            if x_max < lines[i][j]:
                x_max = lines[i][j]
            if y_max < lines[i][j+1]:
                y_max = lines[i][j+1]

    grid = [ [0]*(x_max+2) for i in range(y_max+1)]

    for i in range(len(lines)):
        line =  lines[i]

        if line[0] == line[2]:
            x = line[0]
            for y in range(min([line[1],line[3]]),max([line[1],line[3]])+1):
                grid[y][x] += 1
        else:
            y = line[1]
            for x in range(line[0],line[2]+1):
                grid[y][x] += 1
                y += line[4]

    tick = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] > 1:
                tick+=1
    print(f'answer2 = {tick}')
    return grid

grid = part1(Data)