""" load Data """

data = [[k[0:10],k[10:14]] for k in[ j.split(' ')  for j in [i.replace(' | ',' ').strip() for i in open('Data.txt').readlines() ]]]

""" part 1 """

tick = 0
for i in range(len(data)):
    for j in range(len(data[0][1])):
        for numbers in [2,4,3,7]:
            if len(data[i][1][j]) == numbers:
                tick += 1
                
print(f'answer1 = {tick}')

""" part 2 """

def digitsolver(codes,digits):
    tick = [0]*7
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for j in range(len(codes)):
        if len(codes[j]) == 2:
            one = [i for i in codes[j]]
        if len(codes[j]) == 3:
            seven = [i for i in codes[j]]
        if len(codes[j]) == 4:
            four = [i for i in codes[j]]
        if len(codes[j]) == 7:
            eight = [i for i in codes[j]]

        if 'a' in codes[j]:
            tick[0] += 1
        if 'b' in codes[j]:
            tick[1] += 1
        if 'c' in codes[j]:
            tick[2] += 1
        if 'd' in codes[j]:
            tick[3] += 1
        if 'e' in codes[j]:
            tick[4] += 1
        if 'f' in codes[j]:
            tick[5] += 1
        if 'g' in codes[j]:
            tick[6] += 1

    a = list(set(seven).difference(one))[0]

    for i in range(len(tick)):
        if tick[i] == 8 and letters[i] != a:
            c = letters[i]
        if tick[i] == 6:
            b = letters[i]
        if tick[i] == 4:
            e = letters[i]
        if tick[i] == 9:
            f = letters[i]
        if tick[i] == 7:
            if letters[i] not in four:
                d = letters[i]
            else:
                g = letters[i]

    zero = [a, b, c, e, f, g]
    two = [a,c,d,e,g]
    three = [a, c, d, f, g]
    five = [a, b, d, f, g]
    six = [a, b, d, e, f, g]
    nine = [a, b, c, d, f, g]
    numbers = [zero,one,two,three,four,five,six,seven,eight,nine]
    
    finalnumber = [0]*4
    for j in range(len(digits)):
        for i in range(len(numbers)):
            if set(digits[j]) == set(numbers[i]):
                finalnumber[j] += i
    output = finalnumber[0]*1000 + finalnumber[1]*100+ finalnumber[2]*10 +finalnumber[3]
    return output

sum =0
for i in range(len(data)):
    sum += digitsolver(data[i][0],data[i][1])

print(f'answer2 = {sum}')


            
