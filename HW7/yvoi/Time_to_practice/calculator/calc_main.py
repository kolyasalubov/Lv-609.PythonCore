import calc_functions as calc


while True:
    user_choice = input("Choose operation you want to do (+, -, *, /, q(quit): ")
    if user_choice == "+":
        calc.plus()
    elif user_choice == "-":
        calc.minus()
    elif user_choice == "*":
        calc.multiplication()
    elif user_choice == "/":
        calc.dividing()
    elif user_choice == "q":
        print("Program finished")
        break
    else:
        print("Error! Invalid key")
