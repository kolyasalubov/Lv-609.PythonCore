final_number = int(input("Please input a number: "))
i = 1 
result = 1
for i in range(1, final_number+1):
    if i <= final_number:
        result *= i
        i += 1
print(result)