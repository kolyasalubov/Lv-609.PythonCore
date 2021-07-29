import calc1

value = int(input("1-addition, 2-subtraction, 3-multiplication, 4-division: "))

while value not in range(1, 5):
    print("Wrong value.")
    value = int(input("1-addition, 2-subtraction, 3-multiplication, 4-division: "))
    if value == 1:
        print(calc1.addition(int(input("First number: ")), int(input("Second number: "))))
    elif value == 2:
        print(calc1.subtraction(int(input("First number: ")), int(input("Second number: "))))
    elif value == 3:
        print(calc1.multiplication(int(input("First number: ")), int(input("Second number: "))))
    elif value == 4:
        print(calc1.division(int(input("First number: ")), int(input("Second number: "))))
