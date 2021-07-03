# Частково рішення прийшло з допомогою гугла

number = int(input("Введіть число: "))
fibonacci_numbers = [0, 1]
a = 0
b = 1
for i in range(2, number):
    c = a + b
    a = b
    b = c
    fibonacci_numbers.append(b)
print(*fibonacci_numbers)
