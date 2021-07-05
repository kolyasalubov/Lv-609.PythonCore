number = int(input("Please enter number: "))
list = [0, 1]
for i in range(2, number+1):
    if (list[i-1]+list[i-2]) <= number:
        list.append(list[i-1]+list[i-2]) 
    else:
        break
print(list)