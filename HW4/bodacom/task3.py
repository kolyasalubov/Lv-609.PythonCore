# HW4 task 3
# Done

# Task3. Print Fibonacci numbers up to the entered number n, 
# using cycles. 
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.) 

# Counts Fibbonaci numbers up to given by user element number

# Ask for number of elements in the row
int_number = int(input("Послідовність Фібоначі до якого елементу? "))
# print(int_number)

# Initialise two basic elements
fibonacci_elements = [0, 1]

# Check the input and print requested number of elements
if int_number <= 0:
    print("Введене число менше або рівне нулю. Єлементи відсутні.")

elif int_number == 1:
    print(fibonacci_elements[0])

elif int_number == 2:
    print(fibonacci_elements)

else:
    i = 2
    while i < int_number:
        fibonacci_elements.append(int(fibonacci_elements[i-1]) + int(fibonacci_elements[i-2]))
        i+=1
    print(fibonacci_elements)
    