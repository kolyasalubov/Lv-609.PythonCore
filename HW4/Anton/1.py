print('WARNING: WRITE ONLY INTEGERS!\n')
num = int(input('Number:'))
fact = 1
for n in range(1,num+1):
    fact = fact * n
print(f'{num}! = {fact}')