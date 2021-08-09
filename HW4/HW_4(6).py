num_a = 0
num_b = 1
number = int(input("Enter number: "))
for item in range(0, number-1):
    num_a, num_b = num_b, num_a + num_b
    print(num_a, end=" ")
