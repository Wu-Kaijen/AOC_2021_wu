""" import data (now in .txt format) """
output = [ i.strip() for i in open('Data_test.txt').readlines()]

# """ Part 1 clean version """
def upordown(input,i):
    a = [ int(j[i]) for j in input]
    if sum(a) > len(input)/2:
        return '1'
    elif sum(a) < len(input)/2:
        return '0'
    return '1'

gamma =''
for i in range(len(output[0])):
    gamma += upordown(output,i)
    epsilon = str( int('1' *len(output[0])) - int(gamma))

print(f'epsilon = {int(epsilon,2)}, gamma = {int(gamma,2)}, solution = {int(epsilon,2)*int(gamma,2)}')

# """ Part 2 """
# def sorter(values,i):
#     tick=0
#     new_values = []
#     for j in range(len(values)):
#         tick += int(values[j][i])
    
#     if tick > len(values)/2:
#         for j in range(len(values)):
#             if values[j][i] == '1':
#                 new_values.append(values[j])

#     elif tick < len(values)/2: 
#         for j in range(len(values)):
#             if values[j][i] == '0':
#                 new_values.append(values[j])

#     else:  
#         for j in range(len(values)):
#             if values[j][i] == '1':
#                 new_values.append(values[j])
#     return new_values
    
# def sorter2(values,i):
#     tick=0
#     new_values = []
#     for j in range(len(values)):
#         tick += int(values[j][i])
    
#     if tick > len(values)/2:
#         for j in range(len(values)):
#             if values[j][i] == '0':
#                 new_values.append(values[j])

#     elif tick < len(values)/2: 
#         for j in range(len(values)):
#             if values[j][i] == '1':
#                 new_values.append(values[j])

#     else:  
#         for j in range(len(values)):
#             if values[j][i] == '0':
#                 new_values.append(values[j])
#     return new_values

# oxygen = output


# for i in range(len(oxygen[0])):
#     oxygen_val = [0]*len(oxygen[0])
#     oxygen = sorter(oxygen,i)
#     if len(oxygen) == 1:
#         print(oxygen)
#         for j in range(len(oxygen[0])):
#             oxygen_val[j] = int(oxygen[0][j]) 
#         ox = (binatodeci(oxygen_val))
#         break

# co2 = output

# for i in range(len(co2[0])):
#     co2_val = [0]*len(co2[0])
#     co2 = sorter2(co2,i)
#     if len(co2) == 1:
#         for j in range(len(co2[0])):
#             co2_val[j] = int(co2[0][j]) 
#         co = (binatodeci(co2_val))
#         break

# print(co*ox)
