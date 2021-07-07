even = set()
odd = set()
no_divisible = set()

for x in range(1, 11):
    if x % 2 == 0: even.add(x)
    if x % 3 == 0: odd.add(x)
    if x % 2 != 0 and x % 3 != 0: no_divisible.add(x)
print(even)
print(odd)
print(no_divisible)