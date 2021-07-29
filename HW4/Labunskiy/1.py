
a_given_number = int(input("Enter the number in this line :"))
result_of_evaluating = 1

for multiplier in range(2, a_given_number+1):
    result_of_evaluating *= int(multiplier)

print(result_of_evaluating)
