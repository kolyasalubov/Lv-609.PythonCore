import calculator

users_choice = input("Please, choose an action you'd like to do:"
                     "\na. Addition"
                     "\nb. Subtraction"
                     "\nc. Multiplication"
                     "\nd. Division"
                     "\nYour choice - ")
if users_choice == "a":
    print(calculator.sum_res())
elif users_choice == "b":
    print(calculator.subtraction_res())
elif users_choice == "c":
    print(calculator.multiplication_res())
elif users_choice == "d":
    print(calculator.division_res())
else:
    print("Your input is wrong. Try again later.")
