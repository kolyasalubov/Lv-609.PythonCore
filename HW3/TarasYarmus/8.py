first_number = int(input('Enter your first number: '))
last_number = int(input('Enter your last number: '))

result = list(range(first_number, last_number + 1))
print(f'''This is your list: \n {result}''')



i = 0
while i < len(result):
    result[i] = float(result[i])
    i += 1
print(f'''This is your list in float type: \n {result}''')