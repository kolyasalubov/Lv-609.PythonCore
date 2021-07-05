# num = int(input('Enter number: '))
num = 55
first = 0
second = 1
result = 0
num_list = [0,1]
while result != num:
    result = first + second
    first = second
    second = result
    num_list.append(result)
    
print(num_list)