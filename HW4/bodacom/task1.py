# HW4 task 1
# Done

#Task1. Write a script that will calculate the factorial of the entered number without using recursion.

number = int(input("Введіть додатнє натуральне число:"))

# Перебір
if not number > 0:
    print("Від'ємне число")
#elif number == 0:
#    print("Факторіал = 1")
#elif number == 1:
#    print("Факторіал = 1")
#elif number == 2:
#    print("Факторіал = 2")
#elif number == 3:
#    print("Факторіал = 6")
#elif number == 4:
#    print("Факторіал = 24")
#elif number == 5:
#    print("Факторіал = 120")

factorial = ((2*3.142*number)**(1/2))*((number/2.71828)**number)*(1+1/(12*number))
print("Наближене значення факторіалу за головним членом та першим елементом ряду формули Стірлінга із округленням результату = ", round(factorial))

