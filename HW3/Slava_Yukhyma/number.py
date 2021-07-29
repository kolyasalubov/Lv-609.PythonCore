# 1.MULTIPLICATION OF ALL COMPONENTS

numb = 1234

# перетворення до рядка
numb_str = str(numb)

# перетворення до списку, щоб проітерувати
number = list(numb_str)

# ВИРІШЕННЯ
i = 0
result = 1
for num in number:
    result = result * int(number[i])
    i += 1

print('Результат множення всіх компонентів числа', result)

# простіший варіант, перебираємо елементи рядка,
# при операції мнoження - приводимо елемент до числа (int).
number = 1234
number = str(number)
result = 1
for num in number:
    result *= int(num)  # result = result * int(num)
print('Результат множення всіх компонентів числа', result)

print("*"*50)

# 2.REVERSED NUMBER
number = 123456
number = str(number)

reversed_num_str = number[::-1]
print(reversed_num_str)

number = int(reversed_num_str)
print(type(number))

# спробувати написати функцію


def reverse_num(your_number):
    reverse_num = str(your_number)
    reverse_num = int(reverse_num[::-1])
    print(reverse_num)


reverse_num(123456789)

# 3.SORTED NUMBER
number = 2948576
number_str = str(number)
number_list = list(number_str)
sorted_num = int(''.join(sorted(number_list)))
print('sorted number', sorted_num)
