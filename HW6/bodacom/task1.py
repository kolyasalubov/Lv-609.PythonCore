# HW6 task1

# Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).

def largest(a, b):
    if a == b:
        return "Equal"
    elif a > b:
        return a
    else:
        return b

# For test
# a, b = 2, 3
# 
# print(largest(a, b))