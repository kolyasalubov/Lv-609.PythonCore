parni = set()
ne_parni = set()
ne_dil = set()

for x in range(1, 11):
    if x % 2 == 0: parni.add(x)
    if x % 3 == 0: ne_parni.add(x)
    if x % 2 != 0 and x % 3 != 0: ne_dil.add(x)
print(f"Парні числа: {parni} \nНепарні числа: {ne_parni} \nНе ділиться ні на 2, ні на 3: {ne_dil}")